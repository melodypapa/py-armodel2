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
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ARPackage, cls).deserialize(element)

        # Parse ar_packages (list from container "AR-PACKAGES")
        obj.ar_packages = []
        container = ARObject._find_child_element(element, "AR-PACKAGES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.ar_packages.append(child_value)

        # Parse elements (list from container "ELEMENTS")
        obj.elements = []
        container = ARObject._find_child_element(element, "ELEMENTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.elements.append(child_value)

        # Parse reference_base_refs (list from container "REFERENCE-BASES")
        obj.reference_base_refs = []
        container = ARObject._find_child_element(element, "REFERENCE-BASES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.reference_base_refs.append(child_value)

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
