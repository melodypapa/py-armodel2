"""TDEventSwcInternalBehavior AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_swc import (
    TDEventSwc,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.runnable_entity import (
    RunnableEntity,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements.variable_access import (
    VariableAccess,
)


class TDEventSwcInternalBehavior(TDEventSwc):
    """AUTOSAR TDEventSwcInternalBehavior."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "runnable": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=RunnableEntity,
        ),  # runnable
        "td_event_swc_behavior_type": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (TDEventSwcInternal),
        ),  # tdEventSwcBehaviorType
        "variable_access": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=VariableAccess,
        ),  # variableAccess
    }

    def __init__(self) -> None:
        """Initialize TDEventSwcInternalBehavior."""
        super().__init__()
        self.runnable: Optional[RunnableEntity] = None
        self.td_event_swc_behavior_type: Optional[Any] = None
        self.variable_access: Optional[VariableAccess] = None


class TDEventSwcInternalBehaviorBuilder:
    """Builder for TDEventSwcInternalBehavior."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TDEventSwcInternalBehavior = TDEventSwcInternalBehavior()

    def build(self) -> TDEventSwcInternalBehavior:
        """Build and return TDEventSwcInternalBehavior object.

        Returns:
            TDEventSwcInternalBehavior instance
        """
        # TODO: Add validation
        return self._obj
