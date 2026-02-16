"""TDEventVfbPort AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_vfb import (
    TDEventVfb,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_prototype import (
    PortPrototype,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.BlueprintDedicated.Port.port_prototype_blueprint import (
    PortPrototypeBlueprint,
)


class TDEventVfbPort(TDEventVfb):
    """AUTOSAR TDEventVfbPort."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("is_external", None, True, False, None),  # isExternal
        ("port", None, False, False, PortPrototype),  # port
        ("port_prototype", None, False, False, PortPrototypeBlueprint),  # portPrototype
    ]

    def __init__(self) -> None:
        """Initialize TDEventVfbPort."""
        super().__init__()
        self.is_external: Optional[Boolean] = None
        self.port: Optional[PortPrototype] = None
        self.port_prototype: Optional[PortPrototypeBlueprint] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert TDEventVfbPort to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TDEventVfbPort":
        """Create TDEventVfbPort from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            TDEventVfbPort instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to TDEventVfbPort since parent returns ARObject
        return cast("TDEventVfbPort", obj)


class TDEventVfbPortBuilder:
    """Builder for TDEventVfbPort."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TDEventVfbPort = TDEventVfbPort()

    def build(self) -> TDEventVfbPort:
        """Build and return TDEventVfbPort object.

        Returns:
            TDEventVfbPort instance
        """
        # TODO: Add validation
        return self._obj
