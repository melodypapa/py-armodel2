"""ARPackage AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ElementCollection.collectable_element import (
    CollectableElement,
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
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "ar_packages": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=ARPackage,
        ),  # arPackages
        "elements": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=PackageableElement,
        ),  # elements
        "reference_bases": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=ReferenceBase,
        ),  # referenceBases
    }

    def __init__(self) -> None:
        """Initialize ARPackage."""
        super().__init__()
        self.ar_packages: list[ARPackage] = []
        self.elements: list[PackageableElement] = []
        self.reference_bases: list[ReferenceBase] = []


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
