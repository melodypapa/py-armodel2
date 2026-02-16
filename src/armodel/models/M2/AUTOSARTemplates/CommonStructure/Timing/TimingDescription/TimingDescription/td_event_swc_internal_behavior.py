"""TDEventSwcInternalBehavior AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
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
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("runnable", None, False, False, RunnableEntity),  # runnable
        ("td_event_swc_behavior_type", None, False, False, any (TDEventSwcInternal)),  # tdEventSwcBehaviorType
        ("variable_access", None, False, False, VariableAccess),  # variableAccess
    ]

    def __init__(self) -> None:
        """Initialize TDEventSwcInternalBehavior."""
        super().__init__()
        self.runnable: Optional[RunnableEntity] = None
        self.td_event_swc_behavior_type: Optional[Any] = None
        self.variable_access: Optional[VariableAccess] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert TDEventSwcInternalBehavior to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TDEventSwcInternalBehavior":
        """Create TDEventSwcInternalBehavior from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            TDEventSwcInternalBehavior instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to TDEventSwcInternalBehavior since parent returns ARObject
        return cast("TDEventSwcInternalBehavior", obj)


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
