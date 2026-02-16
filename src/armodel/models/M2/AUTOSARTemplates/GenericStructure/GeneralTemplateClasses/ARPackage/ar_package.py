"""ARPackage AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ElementCollection.collectable_element import (
    CollectableElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_package import (
    ARPackage,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.packageable_element import (
    PackageableElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.reference_base import (
    ReferenceBase,
)


class ARPackage(CollectableElement):
    """AUTOSAR ARPackage."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("ar_packages", None, False, True, ARPackage),  # arPackages
        ("elements", None, False, True, PackageableElement),  # elements
        ("reference_bases", None, False, True, ReferenceBase),  # referenceBases
    ]

    def __init__(self) -> None:
        """Initialize ARPackage."""
        super().__init__()
        self.ar_packages: list[ARPackage] = []
        self.elements: list[PackageableElement] = []
        self.reference_bases: list[ReferenceBase] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ARPackage to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ARPackage":
        """Create ARPackage from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ARPackage instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ARPackage since parent returns ARObject
        return cast("ARPackage", obj)


class ARPackageBuilder:
    """Builder for ARPackage."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ARPackage = ARPackage()

    def build(self) -> ARPackage:
        """Build and return ARPackage object.

        Returns:
            ARPackage instance
        """
        # TODO: Add validation
        return self._obj
