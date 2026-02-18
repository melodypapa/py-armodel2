"""Implementation AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 126)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 619)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2029)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 449)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Implementation.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Implementation import (
    ProgramminglanguageEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    RevisionLabelString,
    String,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.BuildActionManifest.build_action_manifest import (
    BuildActionManifest,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Implementation.code import (
    Code,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Implementation.compiler import (
    Compiler,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Implementation.dependency_on_artifact import (
    DependencyOnArtifact,
)
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_element import (
    HwElement,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Implementation.linker import (
    Linker,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.mc_support_data import (
    McSupportData,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.resource_consumption import (
    ResourceConsumption,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.SwcBswMapping.swc_bsw_mapping import (
    SwcBswMapping,
)
from abc import ABC, abstractmethod


class Implementation(ARElement, ABC):
    """AUTOSAR Implementation."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    build_action_manifest: Optional[BuildActionManifest]
    code_descriptors: list[Code]
    compilers: list[Compiler]
    generated_refs: list[ARRef]
    hw_elements: list[HwElement]
    linkers: list[Linker]
    mc_support: Optional[McSupportData]
    programming: Optional[ProgramminglanguageEnum]
    required_artifact_refs: list[ARRef]
    required_refs: list[ARRef]
    resource: Optional[ResourceConsumption]
    swc_bsw_ref: Optional[ARRef]
    sw_version: Optional[RevisionLabelString]
    used_code_generator: Optional[String]
    vendor_id: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize Implementation."""
        super().__init__()
        self.build_action_manifest: Optional[BuildActionManifest] = None
        self.code_descriptors: list[Code] = []
        self.compilers: list[Compiler] = []
        self.generated_refs: list[ARRef] = []
        self.hw_elements: list[HwElement] = []
        self.linkers: list[Linker] = []
        self.mc_support: Optional[McSupportData] = None
        self.programming: Optional[ProgramminglanguageEnum] = None
        self.required_artifact_refs: list[ARRef] = []
        self.required_refs: list[ARRef] = []
        self.resource: Optional[ResourceConsumption] = None
        self.swc_bsw_ref: Optional[ARRef] = None
        self.sw_version: Optional[RevisionLabelString] = None
        self.used_code_generator: Optional[String] = None
        self.vendor_id: Optional[PositiveInteger] = None


class ImplementationBuilder:
    """Builder for Implementation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Implementation = Implementation()

    def build(self) -> Implementation:
        """Build and return Implementation object.

        Returns:
            Implementation instance
        """
        # TODO: Add validation
        return self._obj
