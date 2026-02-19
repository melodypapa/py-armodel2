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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
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
    @classmethod
    def deserialize(cls, element: ET.Element) -> "Implementation":
        """Deserialize XML element to Implementation object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Implementation object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse build_action_manifest
        child = ARObject._find_child_element(element, "BUILD-ACTION-MANIFEST")
        if child is not None:
            build_action_manifest_value = ARObject._deserialize_by_tag(child, "BuildActionManifest")
            obj.build_action_manifest = build_action_manifest_value

        # Parse code_descriptors (list)
        obj.code_descriptors = []
        for child in ARObject._find_all_child_elements(element, "CODE-DESCRIPTORS"):
            code_descriptors_value = ARObject._deserialize_by_tag(child, "Code")
            obj.code_descriptors.append(code_descriptors_value)

        # Parse compilers (list)
        obj.compilers = []
        for child in ARObject._find_all_child_elements(element, "COMPILERS"):
            compilers_value = ARObject._deserialize_by_tag(child, "Compiler")
            obj.compilers.append(compilers_value)

        # Parse generated_refs (list)
        obj.generated_refs = []
        for child in ARObject._find_all_child_elements(element, "GENERATEDS"):
            generated_refs_value = ARObject._deserialize_by_tag(child, "DependencyOnArtifact")
            obj.generated_refs.append(generated_refs_value)

        # Parse hw_elements (list)
        obj.hw_elements = []
        for child in ARObject._find_all_child_elements(element, "HW-ELEMENTS"):
            hw_elements_value = ARObject._deserialize_by_tag(child, "HwElement")
            obj.hw_elements.append(hw_elements_value)

        # Parse linkers (list)
        obj.linkers = []
        for child in ARObject._find_all_child_elements(element, "LINKERS"):
            linkers_value = ARObject._deserialize_by_tag(child, "Linker")
            obj.linkers.append(linkers_value)

        # Parse mc_support
        child = ARObject._find_child_element(element, "MC-SUPPORT")
        if child is not None:
            mc_support_value = ARObject._deserialize_by_tag(child, "McSupportData")
            obj.mc_support = mc_support_value

        # Parse programming
        child = ARObject._find_child_element(element, "PROGRAMMING")
        if child is not None:
            programming_value = child.text
            obj.programming = programming_value

        # Parse required_artifact_refs (list)
        obj.required_artifact_refs = []
        for child in ARObject._find_all_child_elements(element, "REQUIRED-ARTIFACTS"):
            required_artifact_refs_value = ARObject._deserialize_by_tag(child, "DependencyOnArtifact")
            obj.required_artifact_refs.append(required_artifact_refs_value)

        # Parse required_refs (list)
        obj.required_refs = []
        for child in ARObject._find_all_child_elements(element, "REQUIREDS"):
            required_refs_value = ARObject._deserialize_by_tag(child, "DependencyOnArtifact")
            obj.required_refs.append(required_refs_value)

        # Parse resource
        child = ARObject._find_child_element(element, "RESOURCE")
        if child is not None:
            resource_value = ARObject._deserialize_by_tag(child, "ResourceConsumption")
            obj.resource = resource_value

        # Parse swc_bsw_ref
        child = ARObject._find_child_element(element, "SWC-BSW")
        if child is not None:
            swc_bsw_ref_value = ARObject._deserialize_by_tag(child, "SwcBswMapping")
            obj.swc_bsw_ref = swc_bsw_ref_value

        # Parse sw_version
        child = ARObject._find_child_element(element, "SW-VERSION")
        if child is not None:
            sw_version_value = child.text
            obj.sw_version = sw_version_value

        # Parse used_code_generator
        child = ARObject._find_child_element(element, "USED-CODE-GENERATOR")
        if child is not None:
            used_code_generator_value = child.text
            obj.used_code_generator = used_code_generator_value

        # Parse vendor_id
        child = ARObject._find_child_element(element, "VENDOR-ID")
        if child is not None:
            vendor_id_value = child.text
            obj.vendor_id = vendor_id_value

        return obj



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
