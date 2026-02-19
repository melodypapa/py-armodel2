"""ARPackage AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 300)
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 297)
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 286)
  - AUTOSAR_CP_TPS_ECUResourceTemplate.pdf (page 58)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 967)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 1992)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 203)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 53)
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 55)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 156)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_ARPackage.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ElementCollection.collectable_element import (
    CollectableElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.packageable_element import (
    PackageableElement,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.reference_base import (
        ReferenceBase,
    )



class ARPackage(CollectableElement):
    """AUTOSAR ARPackage."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    ar_packages: list[ARPackage]
    elements: list[PackageableElement]
    reference_base_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize ARPackage."""
        super().__init__()
        self.ar_packages: list[ARPackage] = []
        self.elements: list[PackageableElement] = []
        self.reference_base_refs: list[ARRef] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "ARPackage":
        """Deserialize XML element to ARPackage object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ARPackage object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse ar_packages (list)
        obj.ar_packages = []
        for child in ARObject._find_all_child_elements(element, "AR-PACKAGES"):
            ar_packages_value = ARObject._deserialize_by_tag(child, "ARPackage")
            obj.ar_packages.append(ar_packages_value)

        # Parse elements (list)
        obj.elements = []
        for child in ARObject._find_all_child_elements(element, "ELEMENTS"):
            elements_value = ARObject._deserialize_by_tag(child, "PackageableElement")
            obj.elements.append(elements_value)

        # Parse reference_base_refs (list)
        obj.reference_base_refs = []
        for child in ARObject._find_all_child_elements(element, "REFERENCE-BASES"):
            reference_base_refs_value = ARObject._deserialize_by_tag(child, "ReferenceBase")
            obj.reference_base_refs.append(reference_base_refs_value)

        return obj



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
