**Role:** You are an expert Cloud Architect and Machine Learning Engineer specializing in Google Cloud Platform (GCP).

**Objective:**

I need to initiate a heavy, high-resource Machine Learning training job on GCP for my Workspace project. We need to maximize our budget utilization and spend a substantial portion of our remaining GCP credits on this training phase.

**Critical Constraints & Justifications:**

1. **Credit Expiration (Urgent):** Our GCP credits will expire on the **22nd of this month**. Therefore, we want to scale up the training resources (using high-end GPUs/TPUs, memory-optimized machine types, or larger cluster configurations) to accelerate our training and fully utilize these credits before they disappear.  
2. **Asynchronous Execution & Handover:** \- I will be shutting down my current local computer at **18:00 (6:00 PM) today**.  
   * I will log in from a completely different computer later to monitor, verify, and continue managing this training.  
   * **Crucial Requirement:** The training job **must not stop** when I disconnect or turn off my current machine. It must run fully asynchronously on GCP's infrastructure.  
3. **Tooling Constraint:** You **must** provide the instructions and commands exclusively using the **GCP CLI (gcloud)**. Do not use the web console for deployment.

**What I need from you:**

1. **Infrastructure Strategy:** Recommend a GCP service that supports fully asynchronous, high-credit-utilization training jobs via CLI.  
2. **GCP CLI (gcloud) Commands:**  
   * Provide the exact gcloud command to check the job status, view streaming logs, and confirm the training progress from my other computer later.  
3. **Resilience Plan:** Ensure that if the training requires multi-stage execution, it is configured to auto-save checkpoints to a Google Cloud Storage (GCS) bucket, so I don't lose any progress if we need to resume or tweak it from the second computer.