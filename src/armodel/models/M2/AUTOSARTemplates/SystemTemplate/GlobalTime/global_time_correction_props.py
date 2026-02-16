"""GlobalTimeCorrectionProps AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    TimeValue,
)


class GlobalTimeCorrectionProps(ARObject):
    """AUTOSAR GlobalTimeCorrectionProps."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("offset_correction", None, True, False, None),  # offsetCorrection
        ("rate_correction", None, True, False, None),  # rateCorrection
        ("rate_corrections", None, True, False, None),  # rateCorrections
    ]

    def __init__(self) -> None:
        """Initialize GlobalTimeCorrectionProps."""
        super().__init__()
        self.offset_correction: Optional[TimeValue] = None
        self.rate_correction: Optional[TimeValue] = None
        self.rate_corrections: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert GlobalTimeCorrectionProps to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "GlobalTimeCorrectionProps":
        """Create GlobalTimeCorrectionProps from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            GlobalTimeCorrectionProps instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to GlobalTimeCorrectionProps since parent returns ARObject
        return cast("GlobalTimeCorrectionProps", obj)


class GlobalTimeCorrectionPropsBuilder:
    """Builder for GlobalTimeCorrectionProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: GlobalTimeCorrectionProps = GlobalTimeCorrectionProps()

    def build(self) -> GlobalTimeCorrectionProps:
        """Build and return GlobalTimeCorrectionProps object.

        Returns:
            GlobalTimeCorrectionProps instance
        """
        # TODO: Add validation
        return self._obj
