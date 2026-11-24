from dataclasses import dataclass, field
 
@dataclass
class WorkflowState:
    request: str
    facts: list[str] = field(default_factory=list)
    draft: str = ''
    approved: bool = False
 
state = WorkflowState('Summarize local AI benefits')
state.facts.append('Can keep selected data on-device')
state.facts.append('Requires suitable local hardware')
state.draft = '; '.join(state.facts)
print('Facts:', len(state.facts))
print('Draft:', state.draft)
print('Approved:', state.approved)

