"""FMFeatureMapAssertion AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)


class FMFeatureMapAssertion(Identifiable):
    """AUTOSAR FMFeatureMapAssertion."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("fm_syscond_and_sw_systemconsts", None, False, False, any (FMConditionByFeatures)),  # fmSyscondAndSwSystemconsts
    ]

    def __init__(self) -> None:
        """Initialize FMFeatureMapAssertion."""
        super().__init__()
        self.fm_syscond_and_sw_systemconsts: Optional[Any] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert FMFeatureMapAssertion to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FMFeatureMapAssertion":
        """Create FMFeatureMapAssertion from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            FMFeatureMapAssertion instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to FMFeatureMapAssertion since parent returns ARObject
        return cast("FMFeatureMapAssertion", obj)


class FMFeatureMapAssertionBuilder:
    """Builder for FMFeatureMapAssertion."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FMFeatureMapAssertion = FMFeatureMapAssertion()

    def build(self) -> FMFeatureMapAssertion:
        """Build and return FMFeatureMapAssertion object.

        Returns:
            FMFeatureMapAssertion instance
        """
        # TODO: Add validation
        return self._obj
