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

    build_action_manifest_ref: Optional[ARRef]
    code_descriptors: list[Code]
    compilers: list[Compiler]
    generated_refs: list[ARRef]
    hw_element_refs: list[ARRef]
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
        self.build_action_manifest_ref: Optional[ARRef] = None
        self.code_descriptors: list[Code] = []
        self.compilers: list[Compiler] = []
        self.generated_refs: list[ARRef] = []
        self.hw_element_refs: list[ARRef] = []
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

    def serialize(self) -> ET.Element:
        """Serialize Implementation to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(Implementation, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize build_action_manifest_ref
        if self.build_action_manifest_ref is not None:
            serialized = ARObject._serialize_item(self.build_action_manifest_ref, "BuildActionManifest")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BUILD-ACTION-MANIFEST-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize code_descriptors (list to container "CODE-DESCRIPTORS")
        if self.code_descriptors:
            wrapper = ET.Element("CODE-DESCRIPTORS")
            for item in self.code_descriptors:
                serialized = ARObject._serialize_item(item, "Code")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize compilers (list to container "COMPILERS")
        if self.compilers:
            wrapper = ET.Element("COMPILERS")
            for item in self.compilers:
                serialized = ARObject._serialize_item(item, "Compiler")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize generated_refs (list to container "GENERATED-REFS")
        if self.generated_refs:
            wrapper = ET.Element("GENERATED-REFS")
            for item in self.generated_refs:
                serialized = ARObject._serialize_item(item, "DependencyOnArtifact")
                if serialized is not None:
                    child_elem = ET.Element("GENERATED-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize hw_element_refs (list to container "HW-ELEMENT-REFS")
        if self.hw_element_refs:
            wrapper = ET.Element("HW-ELEMENT-REFS")
            for item in self.hw_element_refs:
                serialized = ARObject._serialize_item(item, "HwElement")
                if serialized is not None:
                    child_elem = ET.Element("HW-ELEMENT-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize linkers (list to container "LINKERS")
        if self.linkers:
            wrapper = ET.Element("LINKERS")
            for item in self.linkers:
                serialized = ARObject._serialize_item(item, "Linker")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize mc_support
        if self.mc_support is not None:
            serialized = ARObject._serialize_item(self.mc_support, "McSupportData")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MC-SUPPORT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize programming
        if self.programming is not None:
            serialized = ARObject._serialize_item(self.programming, "ProgramminglanguageEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PROGRAMMING")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize required_artifact_refs (list to container "REQUIRED-ARTIFACT-REFS")
        if self.required_artifact_refs:
            wrapper = ET.Element("REQUIRED-ARTIFACT-REFS")
            for item in self.required_artifact_refs:
                serialized = ARObject._serialize_item(item, "DependencyOnArtifact")
                if serialized is not None:
                    child_elem = ET.Element("REQUIRED-ARTIFACT-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize required_refs (list to container "REQUIRED-REFS")
        if self.required_refs:
            wrapper = ET.Element("REQUIRED-REFS")
            for item in self.required_refs:
                serialized = ARObject._serialize_item(item, "DependencyOnArtifact")
                if serialized is not None:
                    child_elem = ET.Element("REQUIRED-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize resource
        if self.resource is not None:
            serialized = ARObject._serialize_item(self.resource, "ResourceConsumption")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RESOURCE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize swc_bsw_ref
        if self.swc_bsw_ref is not None:
            serialized = ARObject._serialize_item(self.swc_bsw_ref, "SwcBswMapping")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SWC-BSW-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sw_version
        if self.sw_version is not None:
            serialized = ARObject._serialize_item(self.sw_version, "RevisionLabelString")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-VERSION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize used_code_generator
        if self.used_code_generator is not None:
            serialized = ARObject._serialize_item(self.used_code_generator, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("USED-CODE-GENERATOR")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize vendor_id
        if self.vendor_id is not None:
            serialized = ARObject._serialize_item(self.vendor_id, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VENDOR-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Implementation":
        """Deserialize XML element to Implementation object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Implementation object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(Implementation, cls).deserialize(element)

        # Parse build_action_manifest_ref
        child = ARObject._find_child_element(element, "BUILD-ACTION-MANIFEST-REF")
        if child is not None:
            build_action_manifest_ref_value = ARRef.deserialize(child)
            obj.build_action_manifest_ref = build_action_manifest_ref_value

        # Parse code_descriptors (list from container "CODE-DESCRIPTORS")
        obj.code_descriptors = []
        container = ARObject._find_child_element(element, "CODE-DESCRIPTORS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.code_descriptors.append(child_value)

        # Parse compilers (list from container "COMPILERS")
        obj.compilers = []
        container = ARObject._find_child_element(element, "COMPILERS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.compilers.append(child_value)

        # Parse generated_refs (list from container "GENERATED-REFS")
        obj.generated_refs = []
        container = ARObject._find_child_element(element, "GENERATED-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = ARObject._strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.generated_refs.append(child_value)

        # Parse hw_element_refs (list from container "HW-ELEMENT-REFS")
        obj.hw_element_refs = []
        container = ARObject._find_child_element(element, "HW-ELEMENT-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = ARObject._strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.hw_element_refs.append(child_value)

        # Parse linkers (list from container "LINKERS")
        obj.linkers = []
        container = ARObject._find_child_element(element, "LINKERS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.linkers.append(child_value)

        # Parse mc_support
        child = ARObject._find_child_element(element, "MC-SUPPORT")
        if child is not None:
            mc_support_value = ARObject._deserialize_by_tag(child, "McSupportData")
            obj.mc_support = mc_support_value

        # Parse programming
        child = ARObject._find_child_element(element, "PROGRAMMING")
        if child is not None:
            programming_value = ProgramminglanguageEnum.deserialize(child)
            obj.programming = programming_value

        # Parse required_artifact_refs (list from container "REQUIRED-ARTIFACT-REFS")
        obj.required_artifact_refs = []
        container = ARObject._find_child_element(element, "REQUIRED-ARTIFACT-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = ARObject._strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.required_artifact_refs.append(child_value)

        # Parse required_refs (list from container "REQUIRED-REFS")
        obj.required_refs = []
        container = ARObject._find_child_element(element, "REQUIRED-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = ARObject._strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.required_refs.append(child_value)

        # Parse resource
        child = ARObject._find_child_element(element, "RESOURCE")
        if child is not None:
            resource_value = ARObject._deserialize_by_tag(child, "ResourceConsumption")
            obj.resource = resource_value

        # Parse swc_bsw_ref
        child = ARObject._find_child_element(element, "SWC-BSW-REF")
        if child is not None:
            swc_bsw_ref_value = ARRef.deserialize(child)
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
