"""System AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 349)
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 331)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 1007)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 40)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 249)
  - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (page 17)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 476)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ByteOrderEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    RevisionLabelString,
)
from armodel.models.M2.MSR.Documentation.Chapters.chapter import (
    Chapter,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.client_id_definition_set import (
    ClientIdDefinitionSet,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.cp_software_cluster import (
    CpSoftwareCluster,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import (
    FibexElement,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.MeasurementAndCalibration.InterpolationRoutine.interpolation_routine_mapping_set import (
    InterpolationRoutineMappingSet,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.j1939_shared_address_cluster import (
    J1939SharedAddressCluster,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.root_sw_composition_prototype import (
    RootSwCompositionPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.system_mapping import (
    SystemMapping,
)


class System(ARElement):
    """AUTOSAR System."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    client_id_definition_set_refs: list[ARRef]
    container_i_pdu_header_byte_order: Optional[ByteOrderEnum]
    ecu_extract_version: Optional[RevisionLabelString]
    fibex_element_refs: list[ARRef]
    interpolation_routine_mapping_set_refs: list[ARRef]
    j1939_shared_address_clusters: list[J1939SharedAddressCluster]
    mapping_refs: list[ARRef]
    pnc_vector_length: Optional[PositiveInteger]
    pnc_vector_offset: Optional[PositiveInteger]
    root_software_composition: Optional[RootSwCompositionPrototype]
    sw_cluster_refs: list[ARRef]
    system_documentations: list[Chapter]
    system_version: Optional[RevisionLabelString]
    def __init__(self) -> None:
        """Initialize System."""
        super().__init__()
        self.client_id_definition_set_refs: list[ARRef] = []
        self.container_i_pdu_header_byte_order: Optional[ByteOrderEnum] = None
        self.ecu_extract_version: Optional[RevisionLabelString] = None
        self.fibex_element_refs: list[ARRef] = []
        self.interpolation_routine_mapping_set_refs: list[ARRef] = []
        self.j1939_shared_address_clusters: list[J1939SharedAddressCluster] = []
        self.mapping_refs: list[ARRef] = []
        self.pnc_vector_length: Optional[PositiveInteger] = None
        self.pnc_vector_offset: Optional[PositiveInteger] = None
        self.root_software_composition: Optional[RootSwCompositionPrototype] = None
        self.sw_cluster_refs: list[ARRef] = []
        self.system_documentations: list[Chapter] = []
        self.system_version: Optional[RevisionLabelString] = None

    def serialize(self) -> ET.Element:
        """Serialize System to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(System, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize client_id_definition_set_refs (list to container "CLIENT-ID-DEFINITION-SET-REFS")
        if self.client_id_definition_set_refs:
            wrapper = ET.Element("CLIENT-ID-DEFINITION-SET-REFS")
            for item in self.client_id_definition_set_refs:
                serialized = SerializationHelper.serialize_item(item, "ClientIdDefinitionSet")
                if serialized is not None:
                    child_elem = ET.Element("CLIENT-ID-DEFINITION-SET-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize container_i_pdu_header_byte_order
        if self.container_i_pdu_header_byte_order is not None:
            serialized = SerializationHelper.serialize_item(self.container_i_pdu_header_byte_order, "ByteOrderEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONTAINER-I-PDU-HEADER-BYTE-ORDER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize ecu_extract_version
        if self.ecu_extract_version is not None:
            serialized = SerializationHelper.serialize_item(self.ecu_extract_version, "RevisionLabelString")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ECU-EXTRACT-VERSION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize fibex_element_refs (list to container "FIBEX-ELEMENT-REFS")
        if self.fibex_element_refs:
            wrapper = ET.Element("FIBEX-ELEMENT-REFS")
            for item in self.fibex_element_refs:
                serialized = SerializationHelper.serialize_item(item, "FibexElement")
                if serialized is not None:
                    child_elem = ET.Element("FIBEX-ELEMENT-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize interpolation_routine_mapping_set_refs (list to container "INTERPOLATION-ROUTINE-MAPPING-SET-REFS")
        if self.interpolation_routine_mapping_set_refs:
            wrapper = ET.Element("INTERPOLATION-ROUTINE-MAPPING-SET-REFS")
            for item in self.interpolation_routine_mapping_set_refs:
                serialized = SerializationHelper.serialize_item(item, "InterpolationRoutineMappingSet")
                if serialized is not None:
                    child_elem = ET.Element("INTERPOLATION-ROUTINE-MAPPING-SET-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize j1939_shared_address_clusters (list to container "J1939-SHARED-ADDRESS-CLUSTERS")
        if self.j1939_shared_address_clusters:
            wrapper = ET.Element("J1939-SHARED-ADDRESS-CLUSTERS")
            for item in self.j1939_shared_address_clusters:
                serialized = SerializationHelper.serialize_item(item, "J1939SharedAddressCluster")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize mapping_refs (list to container "MAPPING-REFS")
        if self.mapping_refs:
            wrapper = ET.Element("MAPPING-REFS")
            for item in self.mapping_refs:
                serialized = SerializationHelper.serialize_item(item, "SystemMapping")
                if serialized is not None:
                    child_elem = ET.Element("MAPPING-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize pnc_vector_length
        if self.pnc_vector_length is not None:
            serialized = SerializationHelper.serialize_item(self.pnc_vector_length, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PNC-VECTOR-LENGTH")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize pnc_vector_offset
        if self.pnc_vector_offset is not None:
            serialized = SerializationHelper.serialize_item(self.pnc_vector_offset, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PNC-VECTOR-OFFSET")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize root_software_composition
        if self.root_software_composition is not None:
            serialized = SerializationHelper.serialize_item(self.root_software_composition, "RootSwCompositionPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ROOT-SOFTWARE-COMPOSITION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sw_cluster_refs (list to container "SW-CLUSTER-REFS")
        if self.sw_cluster_refs:
            wrapper = ET.Element("SW-CLUSTER-REFS")
            for item in self.sw_cluster_refs:
                serialized = SerializationHelper.serialize_item(item, "CpSoftwareCluster")
                if serialized is not None:
                    child_elem = ET.Element("SW-CLUSTER-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize system_documentations (list to container "SYSTEM-DOCUMENTATIONS")
        if self.system_documentations:
            wrapper = ET.Element("SYSTEM-DOCUMENTATIONS")
            for item in self.system_documentations:
                serialized = SerializationHelper.serialize_item(item, "Chapter")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize system_version
        if self.system_version is not None:
            serialized = SerializationHelper.serialize_item(self.system_version, "RevisionLabelString")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SYSTEM-VERSION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "System":
        """Deserialize XML element to System object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized System object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(System, cls).deserialize(element)

        # Parse client_id_definition_set_refs (list from container "CLIENT-ID-DEFINITION-SET-REFS")
        obj.client_id_definition_set_refs = []
        container = SerializationHelper.find_child_element(element, "CLIENT-ID-DEFINITION-SET-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.client_id_definition_set_refs.append(child_value)

        # Parse container_i_pdu_header_byte_order
        child = SerializationHelper.find_child_element(element, "CONTAINER-I-PDU-HEADER-BYTE-ORDER")
        if child is not None:
            container_i_pdu_header_byte_order_value = ByteOrderEnum.deserialize(child)
            obj.container_i_pdu_header_byte_order = container_i_pdu_header_byte_order_value

        # Parse ecu_extract_version
        child = SerializationHelper.find_child_element(element, "ECU-EXTRACT-VERSION")
        if child is not None:
            ecu_extract_version_value = child.text
            obj.ecu_extract_version = ecu_extract_version_value

        # Parse fibex_element_refs (list from container "FIBEX-ELEMENT-REFS")
        obj.fibex_element_refs = []
        container = SerializationHelper.find_child_element(element, "FIBEX-ELEMENT-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.fibex_element_refs.append(child_value)

        # Parse interpolation_routine_mapping_set_refs (list from container "INTERPOLATION-ROUTINE-MAPPING-SET-REFS")
        obj.interpolation_routine_mapping_set_refs = []
        container = SerializationHelper.find_child_element(element, "INTERPOLATION-ROUTINE-MAPPING-SET-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.interpolation_routine_mapping_set_refs.append(child_value)

        # Parse j1939_shared_address_clusters (list from container "J1939-SHARED-ADDRESS-CLUSTERS")
        obj.j1939_shared_address_clusters = []
        container = SerializationHelper.find_child_element(element, "J1939-SHARED-ADDRESS-CLUSTERS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.j1939_shared_address_clusters.append(child_value)

        # Parse mapping_refs (list from container "MAPPING-REFS")
        obj.mapping_refs = []
        container = SerializationHelper.find_child_element(element, "MAPPING-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.mapping_refs.append(child_value)

        # Parse pnc_vector_length
        child = SerializationHelper.find_child_element(element, "PNC-VECTOR-LENGTH")
        if child is not None:
            pnc_vector_length_value = child.text
            obj.pnc_vector_length = pnc_vector_length_value

        # Parse pnc_vector_offset
        child = SerializationHelper.find_child_element(element, "PNC-VECTOR-OFFSET")
        if child is not None:
            pnc_vector_offset_value = child.text
            obj.pnc_vector_offset = pnc_vector_offset_value

        # Parse root_software_composition
        child = SerializationHelper.find_child_element(element, "ROOT-SOFTWARE-COMPOSITION")
        if child is not None:
            root_software_composition_value = SerializationHelper.deserialize_by_tag(child, "RootSwCompositionPrototype")
            obj.root_software_composition = root_software_composition_value

        # Parse sw_cluster_refs (list from container "SW-CLUSTER-REFS")
        obj.sw_cluster_refs = []
        container = SerializationHelper.find_child_element(element, "SW-CLUSTER-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.sw_cluster_refs.append(child_value)

        # Parse system_documentations (list from container "SYSTEM-DOCUMENTATIONS")
        obj.system_documentations = []
        container = SerializationHelper.find_child_element(element, "SYSTEM-DOCUMENTATIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.system_documentations.append(child_value)

        # Parse system_version
        child = SerializationHelper.find_child_element(element, "SYSTEM-VERSION")
        if child is not None:
            system_version_value = child.text
            obj.system_version = system_version_value

        return obj



class SystemBuilder:
    """Builder for System."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: System = System()

    def build(self) -> System:
        """Build and return System object.

        Returns:
            System instance
        """
        # TODO: Add validation
        return self._obj
