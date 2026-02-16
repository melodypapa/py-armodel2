"""ValueGroup AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData.multilanguage_long_name import (
    MultilanguageLongName,
)
from armodel.models.M2.MSR.CalibrationData.CalibrationValue.sw_values import (
    SwValues,
)


class ValueGroup(ARObject):
    """AUTOSAR ValueGroup."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("label", None, False, False, MultilanguageLongName),  # label
        ("vg_contents", None, False, False, SwValues),  # vgContents
    ]

    def __init__(self) -> None:
        """Initialize ValueGroup."""
        super().__init__()
        self.label: Optional[MultilanguageLongName] = None
        self.vg_contents: Optional[SwValues] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ValueGroup to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ValueGroup":
        """Create ValueGroup from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ValueGroup instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ValueGroup since parent returns ARObject
        return cast("ValueGroup", obj)


class ValueGroupBuilder:
    """Builder for ValueGroup."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ValueGroup = ValueGroup()

    def build(self) -> ValueGroup:
        """Build and return ValueGroup object.

        Returns:
            ValueGroup instance
        """
        # TODO: Add validation
        return self._obj
