"""TDEventVariableDataPrototype AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_vfb_port import (
    TDEventVfbPort,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)


class TDEventVariableDataPrototype(TDEventVfbPort):
    """AUTOSAR TDEventVariableDataPrototype."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("data_element", None, False, False, VariableDataPrototype),  # dataElement
        ("td_event_variable_type", None, False, False, any (TDEventVariableData)),  # tdEventVariableType
    ]

    def __init__(self) -> None:
        """Initialize TDEventVariableDataPrototype."""
        super().__init__()
        self.data_element: Optional[VariableDataPrototype] = None
        self.td_event_variable_type: Optional[Any] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert TDEventVariableDataPrototype to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TDEventVariableDataPrototype":
        """Create TDEventVariableDataPrototype from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            TDEventVariableDataPrototype instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to TDEventVariableDataPrototype since parent returns ARObject
        return cast("TDEventVariableDataPrototype", obj)


class TDEventVariableDataPrototypeBuilder:
    """Builder for TDEventVariableDataPrototype."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TDEventVariableDataPrototype = TDEventVariableDataPrototype()

    def build(self) -> TDEventVariableDataPrototype:
        """Build and return TDEventVariableDataPrototype object.

        Returns:
            TDEventVariableDataPrototype instance
        """
        # TODO: Add validation
        return self._obj
