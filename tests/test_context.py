import importlib.machinery, importlib.util, tempfile, unittest, subprocess, json, shutil, io, sys
from unittest.mock import patch
from contextlib import redirect_stdout
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
SCRIPT=ROOT/'bin/context'
class InstallerTests(unittest.TestCase):
    def setUp(self):
        (ROOT/'work').mkdir(exist_ok=True)
        self.temp=tempfile.TemporaryDirectory(dir=ROOT/'work')
        self.home=Path(self.temp.name)/'home';self.home.mkdir()
    def tearDown(self): self.temp.cleanup()
    def run_cli(self,*args,ok=True):
        result=subprocess.run(['python3',str(SCRIPT),*args,'--home',str(self.home)],text=True,capture_output=True)
        if ok:self.assertEqual(result.returncode,0,result.stderr)
        else:self.assertNotEqual(result.returncode,0)
        return result
    def state(self):return json.loads((self.home/'.local/state/my-ai-context/state.json').read_text())
    def test_preview_no_writes(self):
        self.run_cli('install','--targets','claude,codex')
        self.assertEqual(list(self.home.iterdir()),[])
    def test_preserve_idempotent_and_uninstall(self):
        config=self.home/'.claude/CLAUDE.md';config.parent.mkdir();config.write_text('Existing preferences\n')
        self.run_cli('install','--targets','claude','--apply')
        self.assertTrue(config.read_text().startswith('Existing preferences\n'))
        history=len(self.state()['history'])
        self.run_cli('update','--apply')
        self.assertEqual(len(self.state()['history']),history)
        self.run_cli('uninstall','--apply')
        self.assertEqual(config.read_text(),'Existing preferences\n')
        self.assertFalse((self.home/'.claude/skills/my-research/SKILL.md').exists())
    def test_drift_aborts_whole_operation(self):
        self.run_cli('install','--targets','claude','--apply')
        file=self.home/'.claude/skills/my-research/SKILL.md';file.write_text('Local customization')
        self.run_cli('install','--targets','codex','--apply',ok=False)
        self.assertEqual(file.read_text(),'Local customization')
        self.assertFalse((self.home/'.codex/AGENTS.md').exists())
    def test_unmanaged_and_symlink_refused(self):
        file=self.home/'.claude/skills/my-research/SKILL.md';file.parent.mkdir(parents=True);file.write_text('Unmanaged')
        self.run_cli('install','--targets','claude','--apply',ok=False)
        self.assertFalse((self.home/'.claude/CLAUDE.md').exists())
        file.unlink();outside=Path(self.temp.name)/'outside';outside.mkdir()
        (self.home/'.agents').symlink_to(outside,target_is_directory=True)
        self.run_cli('install','--targets','codex','--apply',ok=False)
        self.assertEqual(list(outside.iterdir()),[])
    def test_rollback_incremental_install(self):
        self.run_cli('install','--targets','claude','--apply')
        self.run_cli('install','--targets','codex','--apply')
        self.run_cli('rollback','--apply')
        self.assertTrue((self.home/'.claude/CLAUDE.md').exists())
        self.assertFalse((self.home/'.codex/AGENTS.md').exists())
        self.assertEqual(self.state()['targets'],['claude'])
    def test_source_update_and_rollback(self):
        repo=Path(self.temp.name)/'repo'
        shutil.copytree(ROOT,repo,ignore=shutil.ignore_patterns('.git','work','__pycache__'))
        script=repo/'bin/context'
        def run(*args):
            result=subprocess.run(['python3',str(script),*args,'--home',str(self.home)],text=True,capture_output=True)
            self.assertEqual(result.returncode,0,result.stderr)
        run('install','--targets','claude','--apply')
        dest=self.home/'.claude/skills/my-research/SKILL.md';before=dest.read_bytes()
        source=repo/'skills/my-research/SKILL.md';source.write_text(source.read_text()+'\nApproved update\n')
        run('update','--apply');self.assertIn(b'Approved update',dest.read_bytes())
        run('rollback','--apply');self.assertEqual(dest.read_bytes(),before)
    def test_shadow_override_refused(self):
        p=self.home/'.codex/AGENTS.override.md';p.parent.mkdir();p.write_text('Other profile')
        self.run_cli('install','--targets','codex','--apply',ok=False)
        self.assertFalse((self.home/'.codex/AGENTS.md').exists())
    def test_render_no_placeholders(self):
        self.run_cli('install','--targets','claude','--apply')
        for p in (self.home/'.claude/skills').rglob('*.md'):
            self.assertNotIn('@WORKFLOW:',p.read_text());self.assertNotIn('@PROFILE@',p.read_text());self.assertNotIn('@REPO@',p.read_text())
        data=(self.home/'.claude/skills/my-feature-workflow/references/feature.md').read_text()
        self.assertIn('Thịnh duyệt',data)
    def test_deduplicate_shared_destinations(self):
        self.run_cli('install','--targets','codex,cursor,copilot','--apply')
        self.assertEqual(len(list((self.home/'.agents/skills').glob('*/SKILL.md'))),8)
        self.assertFalse((self.home/'.cursor/skills').exists())
        self.assertFalse((self.home/'.copilot/skills').exists())
    def test_failure_restores_files(self):
        loader=importlib.machinery.SourceFileLoader('context_under_test',str(SCRIPT))
        spec=importlib.util.spec_from_loader(loader.name,loader)
        module=importlib.util.module_from_spec(spec);loader.exec_module(module)
        original=module.atom
        count=0
        def failing(path,data):
            nonlocal count
            count+=1
            if count==3:raise OSError('simulated interrupted write')
            return original(path,data)
        with patch.object(sys,'argv',[str(SCRIPT),'install','--targets','claude','--apply','--home',str(self.home)]),patch.object(module,'atom',failing),redirect_stdout(io.StringIO()):
            with self.assertRaises(OSError):module.main()
        self.assertFalse((self.home/'.claude/CLAUDE.md').exists())
        self.assertEqual(list((self.home/'.claude/skills').rglob('*.md')),[])
        self.assertFalse((self.home/'.local/state/my-ai-context/state.json').exists())
        self.assertFalse((self.home/'.local/state/my-ai-context/apply.lock').exists())
    def test_lock_refuses_second_writer(self):
        lock=self.home/'.local/state/my-ai-context/apply.lock';lock.parent.mkdir(parents=True);lock.write_text('locked')
        self.run_cli('install','--targets','claude','--apply',ok=False)
        self.assertFalse((self.home/'.claude/CLAUDE.md').exists())
    def test_uninstall_rollback(self):
        self.run_cli('install','--targets','claude','--apply')
        self.run_cli('uninstall','--apply')
        self.run_cli('rollback','--apply')
        self.assertTrue((self.home/'.claude/skills/my-research/SKILL.md').exists())
        self.assertEqual(self.state()['targets'],['claude'])
    def test_wrapper_outside_repo_and_space_in_path(self):
        repo=Path(self.temp.name)/'Project with spaces'
        shutil.copytree(ROOT,repo,ignore=shutil.ignore_patterns('.git','work','__pycache__'))
        wrapper=repo/'context.sh'
        result=subprocess.run(['sh',str(wrapper),'status','--home',str(self.home)],cwd=self.temp.name,text=True,capture_output=True)
        self.assertEqual(result.returncode,0,result.stderr)
        self.assertEqual(json.loads(result.stdout)['repo'],str(repo))
    def test_relocation_refreshes_installed_paths(self):
        repo=Path(self.temp.name)/'first location'
        shutil.copytree(ROOT,repo,ignore=shutil.ignore_patterns('.git','work','__pycache__'))
        def run(location,*args):
            result=subprocess.run(['sh',str(location/'context.sh'),*args,'--home',str(self.home)],cwd=self.temp.name,text=True,capture_output=True)
            self.assertEqual(result.returncode,0,result.stderr)
        run(repo,'install','--targets','claude,codex','--apply')
        moved=Path(self.temp.name)/'new location';repo.rename(moved)
        run(moved,'update','--apply')
        for relative in ['.claude/CLAUDE.md','.codex/AGENTS.md','.agents/skills/my-context-maintenance/SKILL.md']:
            data=(self.home/relative).read_text()
            self.assertIn(str(moved),data);self.assertNotIn(str(repo),data)
        run(moved,'status')
    def test_shortcuts_install_status_update(self):
        for name in ['my-install','my-status','my-update']:
            result=subprocess.run(['sh',str(ROOT/name),'--home',str(self.home)],cwd=self.temp.name,text=True,capture_output=True)
            self.assertEqual(result.returncode,0,result.stderr)
            if name=='my-install':self.assertTrue((self.home/'.codex/AGENTS.md').exists())
            if name=='my-status':self.assertEqual(len(json.loads(result.stdout)['installed_targets']),4)
        self.assertEqual(len(self.state()['history']),1)
if __name__=='__main__':unittest.main()
