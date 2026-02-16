"""CanXlFrameTriggeringProps AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class CanXlFrameTriggeringProps(ARObject):
    """AUTOSAR CanXlFrameTriggeringProps."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("acceptance_field", None, True, False, None),  # acceptanceField
        ("priority_id", None, True, False, None),  # priorityId
        ("sdu_type", None, True, False, None),  # sduType
        ("vcid", None, True, False, None),  # vcid
    ]

    def __init__(self) -> None:
        """Initialize CanXlFrameTriggeringProps."""
        super().__init__()
        self.acceptance_field: Optional[PositiveInteger] = None
        self.priority_id: Optional[PositiveInteger] = None
        self.sdu_type: Optional[PositiveInteger] = None
        self.vcid: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert CanXlFrameTriggeringProps to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CanXlFrameTriggeringProps":
        """Create CanXlFrameTriggeringProps from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            CanXlFrameTriggeringProps instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to CanXlFrameTriggeringProps since parent returns ARObject
        return cast("CanXlFrameTriggeringProps", obj)


class CanXlFrameTriggeringPropsBuilder:
    """Builder for CanXlFrameTriggeringProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CanXlFrameTriggeringProps = CanXlFrameTriggeringProps()

    def build(self) -> CanXlFrameTriggeringProps:
        """Build and return CanXlFrameTriggeringProps object.

        Returns:
            CanXlFrameTriggeringProps instance
        """
        # TODO: Add validation
        return self._obj
