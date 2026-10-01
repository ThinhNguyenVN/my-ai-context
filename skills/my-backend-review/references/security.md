# Security review

Review authentication vs authorization at the affected resource boundary, input handling and sensitive logging. Follow the current auth model; do not default to JWT. Include concrete exploit/impact and minimal fix for findings. Never transmit secrets or test with real customer data.
