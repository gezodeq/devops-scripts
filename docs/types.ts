// types.ts
export interface ScriptConfig {
  name: string;
  description: string;
  command: string;
  args: string[];
}

export interface ScriptResult {
  success: boolean;
  message: string;
  output: string;
}

export interface DevOpsScript {
  id: number;
  config: ScriptConfig;
  results: ScriptResult[];
}

export enum ScriptStatus {
  Pending = 'pending',
  Running = 'running',
  Completed = 'completed',
  Failed = 'failed'
}