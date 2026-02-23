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
from armodel.serialization.decorators import ref_conditional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import ARElementBuilder
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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


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
    _fibex_element_refs: list[ARRef]
    interpolation_routine_mapping_set_refs: list[ARRef]
    j1939_shared_address_clusters: list[J1939SharedAddressCluster]
    mappings: list[SystemMapping]
    pnc_vector_length: Optional[PositiveInteger]
    pnc_vector_offset: Optional[PositiveInteger]
    root_software_compositions: list[RootSwCompositionPrototype]
    sw_cluster_refs: list[ARRef]
    system_documentations: list[Chapter]
    system_version: Optional[RevisionLabelString]
    def __init__(self) -> None:
        """Initialize System."""
        super().__init__()
        self.client_id_definition_set_refs: list[ARRef] = []
        self.container_i_pdu_header_byte_order: Optional[ByteOrderEnum] = None
        self.ecu_extract_version: Optional[RevisionLabelString] = None
        self._fibex_element_refs: list[ARRef] = []
        self.interpolation_routine_mapping_set_refs: list[ARRef] = []
        self.j1939_shared_address_clusters: list[J1939SharedAddressCluster] = []
        self.mappings: list[SystemMapping] = []
        self.pnc_vector_length: Optional[PositiveInteger] = None
        self.pnc_vector_offset: Optional[PositiveInteger] = None
        self.root_software_compositions: list[RootSwCompositionPrototype] = []
        self.sw_cluster_refs: list[ARRef] = []
        self.system_documentations: list[Chapter] = []
        self.system_version: Optional[RevisionLabelString] = None
    @property
    @ref_conditional("FIBEX-ELEMENTS")
    def fibex_element_refs(self) -> list[ARRef]:
        """Get fibex_element_refs with ref_conditional wrapper."""
        return self._fibex_element_refs

    @fibex_element_refs.setter
    def fibex_element_refs(self, value: list[ARRef]) -> None:
        """Set fibex_element_refs with ref_conditional wrapper."""
        self._fibex_element_refs = value


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

        # Serialize fibex_element_refs (list to container "FIBEX-ELEMENTS")
        if self.fibex_element_refs:
            wrapper = ET.Element("FIBEX-ELEMENTS")
            for item in self.fibex_element_refs:
                serialized = SerializationHelper.serialize_item(item, "FibexElement")
                if serialized is not None:
                    # Wrap in FIBEX-ELEMENT-REF-CONDITIONAL
                    conditional = ET.Element("FIBEX-ELEMENT-REF-CONDITIONAL")
                    ref_elem = ET.Element("FIBEX-ELEMENT-REF")
                    if hasattr(serialized, 'attrib'):
                        ref_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        ref_elem.text = serialized.text
                    for child in serialized:
                        ref_elem.append(child)
                    conditional.append(ref_elem)
                    wrapper.append(conditional)
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

        # Serialize mappings (list to container "MAPPINGS")
        if self.mappings:
            wrapper = ET.Element("MAPPINGS")
            for item in self.mappings:
                serialized = SerializationHelper.serialize_item(item, "SystemMapping")
                if serialized is not None:
                    wrapper.append(serialized)
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

        # Serialize root_software_compositions (list to container "ROOT-SOFTWARE-COMPOSITIONS")
        if self.root_software_compositions:
            wrapper = ET.Element("ROOT-SOFTWARE-COMPOSITIONS")
            for item in self.root_software_compositions:
                serialized = SerializationHelper.serialize_item(item, "RootSwCompositionPrototype")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

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
                child_element_tag = SerializationHelper.strip_namespace(child.tag)
                if child_element_tag.endswith("-REF") or child_element_tag.endswith("-TREF"):
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

        # Parse fibex_element_refs (list from container "FIBEX-ELEMENTS")
        obj.fibex_element_refs = []
        container = SerializationHelper.find_child_element(element, "FIBEX-ELEMENTS")
        if container is not None:
            for child in container:
                # Unwrap -REF-CONDITIONAL to extract the inner -REF
                child_element_tag = SerializationHelper.strip_namespace(child.tag)
                if child_element_tag == "FIBEX-ELEMENT-REF-CONDITIONAL":
                    ref_child = SerializationHelper.find_child_element(child, "FIBEX-ELEMENT-REF")
                    if ref_child is not None:
                        child_value = ARRef.deserialize(ref_child)
                else:
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.fibex_element_refs.append(child_value)

        # Parse interpolation_routine_mapping_set_refs (list from container "INTERPOLATION-ROUTINE-MAPPING-SET-REFS")
        obj.interpolation_routine_mapping_set_refs = []
        container = SerializationHelper.find_child_element(element, "INTERPOLATION-ROUTINE-MAPPING-SET-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_element_tag = SerializationHelper.strip_namespace(child.tag)
                if child_element_tag.endswith("-REF") or child_element_tag.endswith("-TREF"):
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

        # Parse mappings (list from container "MAPPINGS")
        obj.mappings = []
        container = SerializationHelper.find_child_element(element, "MAPPINGS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.mappings.append(child_value)

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

        # Parse root_software_compositions (list from container "ROOT-SOFTWARE-COMPOSITIONS")
        obj.root_software_compositions = []
        container = SerializationHelper.find_child_element(element, "ROOT-SOFTWARE-COMPOSITIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.root_software_compositions.append(child_value)

        # Parse sw_cluster_refs (list from container "SW-CLUSTER-REFS")
        obj.sw_cluster_refs = []
        container = SerializationHelper.find_child_element(element, "SW-CLUSTER-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_element_tag = SerializationHelper.strip_namespace(child.tag)
                if child_element_tag.endswith("-REF") or child_element_tag.endswith("-TREF"):
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



class SystemBuilder(ARElementBuilder):
    """Builder for System with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: System = System()


    def with_client_id_definition_sets(self, items: list[ClientIdDefinitionSet]) -> "SystemBuilder":
        """Set client_id_definition_sets list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.client_id_definition_sets = list(items) if items else []
        return self

    def with_container_i_pdu_header_byte_order(self, value: Optional[ByteOrderEnum]) -> "SystemBuilder":
        """Set container_i_pdu_header_byte_order attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.container_i_pdu_header_byte_order = value
        return self

    def with_ecu_extract_version(self, value: Optional[RevisionLabelString]) -> "SystemBuilder":
        """Set ecu_extract_version attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.ecu_extract_version = value
        return self

    def with_fibex_elements(self, items: list[FibexElement]) -> "SystemBuilder":
        """Set fibex_elements list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.fibex_elements = list(items) if items else []
        return self

    def with_interpolation_routine_mapping_sets(self, items: list[InterpolationRoutineMappingSet]) -> "SystemBuilder":
        """Set interpolation_routine_mapping_sets list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.interpolation_routine_mapping_sets = list(items) if items else []
        return self

    def with_j1939_shared_address_clusters(self, items: list[J1939SharedAddressCluster]) -> "SystemBuilder":
        """Set j1939_shared_address_clusters list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.j1939_shared_address_clusters = list(items) if items else []
        return self

    def with_mappings(self, items: list[SystemMapping]) -> "SystemBuilder":
        """Set mappings list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.mappings = list(items) if items else []
        return self

    def with_pnc_vector_length(self, value: Optional[PositiveInteger]) -> "SystemBuilder":
        """Set pnc_vector_length attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.pnc_vector_length = value
        return self

    def with_pnc_vector_offset(self, value: Optional[PositiveInteger]) -> "SystemBuilder":
        """Set pnc_vector_offset attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.pnc_vector_offset = value
        return self

    def with_root_software_compositions(self, items: list[RootSwCompositionPrototype]) -> "SystemBuilder":
        """Set root_software_compositions list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.root_software_compositions = list(items) if items else []
        return self

    def with_sw_clusters(self, items: list[CpSoftwareCluster]) -> "SystemBuilder":
        """Set sw_clusters list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.sw_clusters = list(items) if items else []
        return self

    def with_system_documentations(self, items: list[Chapter]) -> "SystemBuilder":
        """Set system_documentations list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.system_documentations = list(items) if items else []
        return self

    def with_system_version(self, value: Optional[RevisionLabelString]) -> "SystemBuilder":
        """Set system_version attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.system_version = value
        return self


    def add_client_id_definition_set(self, item: ClientIdDefinitionSet) -> "SystemBuilder":
        """Add a single item to client_id_definition_sets list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.client_id_definition_sets.append(item)
        return self

    def clear_client_id_definition_sets(self) -> "SystemBuilder":
        """Clear all items from client_id_definition_sets list.

        Returns:
            self for method chaining
        """
        self._obj.client_id_definition_sets = []
        return self

    def add_fibex_element(self, item: FibexElement) -> "SystemBuilder":
        """Add a single item to fibex_elements list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.fibex_elements.append(item)
        return self

    def clear_fibex_elements(self) -> "SystemBuilder":
        """Clear all items from fibex_elements list.

        Returns:
            self for method chaining
        """
        self._obj.fibex_elements = []
        return self

    def add_interpolation_routine_mapping_set(self, item: InterpolationRoutineMappingSet) -> "SystemBuilder":
        """Add a single item to interpolation_routine_mapping_sets list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.interpolation_routine_mapping_sets.append(item)
        return self

    def clear_interpolation_routine_mapping_sets(self) -> "SystemBuilder":
        """Clear all items from interpolation_routine_mapping_sets list.

        Returns:
            self for method chaining
        """
        self._obj.interpolation_routine_mapping_sets = []
        return self

    def add_j1939_shared_address_cluster(self, item: J1939SharedAddressCluster) -> "SystemBuilder":
        """Add a single item to j1939_shared_address_clusters list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.j1939_shared_address_clusters.append(item)
        return self

    def clear_j1939_shared_address_clusters(self) -> "SystemBuilder":
        """Clear all items from j1939_shared_address_clusters list.

        Returns:
            self for method chaining
        """
        self._obj.j1939_shared_address_clusters = []
        return self

    def add_mapping(self, item: SystemMapping) -> "SystemBuilder":
        """Add a single item to mappings list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.mappings.append(item)
        return self

    def clear_mappings(self) -> "SystemBuilder":
        """Clear all items from mappings list.

        Returns:
            self for method chaining
        """
        self._obj.mappings = []
        return self

    def add_root_software_composition(self, item: RootSwCompositionPrototype) -> "SystemBuilder":
        """Add a single item to root_software_compositions list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.root_software_compositions.append(item)
        return self

    def clear_root_software_compositions(self) -> "SystemBuilder":
        """Clear all items from root_software_compositions list.

        Returns:
            self for method chaining
        """
        self._obj.root_software_compositions = []
        return self

    def add_sw_cluster(self, item: CpSoftwareCluster) -> "SystemBuilder":
        """Add a single item to sw_clusters list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.sw_clusters.append(item)
        return self

    def clear_sw_clusters(self) -> "SystemBuilder":
        """Clear all items from sw_clusters list.

        Returns:
            self for method chaining
        """
        self._obj.sw_clusters = []
        return self

    def add_system_documentation(self, item: Chapter) -> "SystemBuilder":
        """Add a single item to system_documentations list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.system_documentations.append(item)
        return self

    def clear_system_documentations(self) -> "SystemBuilder":
        """Clear all items from system_documentations list.

        Returns:
            self for method chaining
        """
        self._obj.system_documentations = []
        return self



    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from typing import get_type_hints
        from armodel.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # Get type hints for the class
        try:
            type_hints_dict = get_type_hints(type(self._obj))
        except Exception:
            # Cannot resolve type hints (e.g., forward references), skip validation
            return

        for attr_name, attr_type in type_hints_dict.items():
            if attr_name.startswith("_"):
                continue

            value = getattr(self._obj, attr_name)

            # Check required fields (not Optional)
            if value is None and not self._is_optional_type(attr_type):
                if mode == BuilderValidationMode.STRICT:
                    raise ValueError(
                        f"Required attribute '{attr_name}' is None"
                    )
                elif mode == BuilderValidationMode.LENIENT:
                    import warnings
                    warnings.warn(
                        f"Required attribute '{attr_name}' is None",
                        UserWarning
                    )

    @staticmethod
    def _is_optional_type(type_hint: Any) -> bool:
        """Check if a type hint is Optional.

        Args:
            type_hint: Type hint to check

        Returns:
            True if type is Optional, False otherwise
        """
        origin = getattr(type_hint, "__origin__", None)
        return origin is Union

    @staticmethod
    def _get_expected_type(type_hint: Any) -> type:
        """Extract expected type from type hint.

        Args:
            type_hint: Type hint to extract from

        Returns:
            Expected type
        """
        if isinstance(type_hint, str):
            return object
        origin = getattr(type_hint, "__origin__", None)
        if origin is Union:
            args = getattr(type_hint, "__args__", [])
            for arg in args:
                if arg is not type(None):
                    return arg
        elif origin is list:
            args = getattr(type_hint, "__args__", [object])
            return args[0] if args else object
        return type_hint if isinstance(type_hint, type) else object


    def build(self) -> System:
        """Build and return the System instance with validation."""
        self._validate_instance()
        pass
        return self._obj