"""ExternalTriggeringPoint AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.Trigger.external_triggering_point import (
    ExternalTriggeringPoint,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration.trigger import (
    Trigger,
)


class ExternalTriggeringPoint(ARObject):
    """AUTOSAR ExternalTriggeringPoint."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("ident", None, False, False, ExternalTriggeringPoint),  # ident
        ("trigger", None, False, False, Trigger),  # trigger
    ]

    def __init__(self) -> None:
        """Initialize ExternalTriggeringPoint."""
        super().__init__()
        self.ident: Optional[ExternalTriggeringPoint] = None
        self.trigger: Optional[Trigger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ExternalTriggeringPoint to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ExternalTriggeringPoint":
        """Create ExternalTriggeringPoint from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ExternalTriggeringPoint instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ExternalTriggeringPoint since parent returns ARObject
        return cast("ExternalTriggeringPoint", obj)


class ExternalTriggeringPointBuilder:
    """Builder for ExternalTriggeringPoint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ExternalTriggeringPoint = ExternalTriggeringPoint()

    def build(self) -> ExternalTriggeringPoint:
        """Build and return ExternalTriggeringPoint object.

        Returns:
            ExternalTriggeringPoint instance
        """
        # TODO: Add validation
        return self._obj
