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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.packageable_element import (
    PackageableElement,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.reference_base import (
        ReferenceBase,
    )



class ARPackage(CollectableElement):
    """AUTOSAR ARPackage."""

    ar_packages: list[ARPackage]
    elements: list[PackageableElement]
    reference_bases: list[ReferenceBase]
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
