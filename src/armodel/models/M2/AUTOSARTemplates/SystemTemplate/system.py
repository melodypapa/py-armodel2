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
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
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
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.MeasurementAndCalibration.InterpolationRoutine.interpolation_routine import (
    InterpolationRoutine,
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

    client_id_refs: list[ARRef]
    container_i_pdu_header_byte: Optional[Any]
    ecu_extract_version: Optional[RevisionLabelString]
    fibex_elements: list[FibexElement]
    interpolation_routines: list[InterpolationRoutine]
    j1939_shared_addresses: list[J1939SharedAddressCluster]
    mapping_refs: list[ARRef]
    pnc_vector: Optional[PositiveInteger]
    pnc_vector_offset: Optional[PositiveInteger]
    root_software: Optional[RootSwCompositionPrototype]
    sw_clusters: list[CpSoftwareCluster]
    systems: list[Chapter]
    system_version: Optional[RevisionLabelString]
    def __init__(self) -> None:
        """Initialize System."""
        super().__init__()
        self.client_id_refs: list[ARRef] = []
        self.container_i_pdu_header_byte: Optional[Any] = None
        self.ecu_extract_version: Optional[RevisionLabelString] = None
        self.fibex_elements: list[FibexElement] = []
        self.interpolation_routines: list[InterpolationRoutine] = []
        self.j1939_shared_addresses: list[J1939SharedAddressCluster] = []
        self.mapping_refs: list[ARRef] = []
        self.pnc_vector: Optional[PositiveInteger] = None
        self.pnc_vector_offset: Optional[PositiveInteger] = None
        self.root_software: Optional[RootSwCompositionPrototype] = None
        self.sw_clusters: list[CpSoftwareCluster] = []
        self.systems: list[Chapter] = []
        self.system_version: Optional[RevisionLabelString] = None
    def serialize(self) -> ET.Element:
        """Serialize System to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(System, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize client_id_refs (list to container "CLIENT-IDS")
        if self.client_id_refs:
            wrapper = ET.Element("CLIENT-IDS")
            for item in self.client_id_refs:
                serialized = ARObject._serialize_item(item, "ClientIdDefinitionSet")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize container_i_pdu_header_byte
        if self.container_i_pdu_header_byte is not None:
            serialized = ARObject._serialize_item(self.container_i_pdu_header_byte, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONTAINER-I-PDU-HEADER-BYTE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize ecu_extract_version
        if self.ecu_extract_version is not None:
            serialized = ARObject._serialize_item(self.ecu_extract_version, "RevisionLabelString")
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

        # Serialize fibex_elements (list to container "FIBEX-ELEMENTS")
        if self.fibex_elements:
            wrapper = ET.Element("FIBEX-ELEMENTS")
            for item in self.fibex_elements:
                serialized = ARObject._serialize_item(item, "FibexElement")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize interpolation_routines (list to container "INTERPOLATION-ROUTINES")
        if self.interpolation_routines:
            wrapper = ET.Element("INTERPOLATION-ROUTINES")
            for item in self.interpolation_routines:
                serialized = ARObject._serialize_item(item, "InterpolationRoutine")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize j1939_shared_addresses (list to container "J1939-SHARED-ADDRESSES")
        if self.j1939_shared_addresses:
            wrapper = ET.Element("J1939-SHARED-ADDRESSES")
            for item in self.j1939_shared_addresses:
                serialized = ARObject._serialize_item(item, "J1939SharedAddressCluster")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize mapping_refs (list to container "MAPPINGS")
        if self.mapping_refs:
            wrapper = ET.Element("MAPPINGS")
            for item in self.mapping_refs:
                serialized = ARObject._serialize_item(item, "SystemMapping")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize pnc_vector
        if self.pnc_vector is not None:
            serialized = ARObject._serialize_item(self.pnc_vector, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PNC-VECTOR")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize pnc_vector_offset
        if self.pnc_vector_offset is not None:
            serialized = ARObject._serialize_item(self.pnc_vector_offset, "PositiveInteger")
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

        # Serialize root_software
        if self.root_software is not None:
            serialized = ARObject._serialize_item(self.root_software, "RootSwCompositionPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ROOT-SOFTWARE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sw_clusters (list to container "SW-CLUSTERS")
        if self.sw_clusters:
            wrapper = ET.Element("SW-CLUSTERS")
            for item in self.sw_clusters:
                serialized = ARObject._serialize_item(item, "CpSoftwareCluster")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize systems (list to container "SYSTEMS")
        if self.systems:
            wrapper = ET.Element("SYSTEMS")
            for item in self.systems:
                serialized = ARObject._serialize_item(item, "Chapter")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize system_version
        if self.system_version is not None:
            serialized = ARObject._serialize_item(self.system_version, "RevisionLabelString")
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

        # Parse client_id_refs (list from container "CLIENT-IDS")
        obj.client_id_refs = []
        container = ARObject._find_child_element(element, "CLIENT-IDS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.client_id_refs.append(child_value)

        # Parse container_i_pdu_header_byte
        child = ARObject._find_child_element(element, "CONTAINER-I-PDU-HEADER-BYTE")
        if child is not None:
            container_i_pdu_header_byte_value = child.text
            obj.container_i_pdu_header_byte = container_i_pdu_header_byte_value

        # Parse ecu_extract_version
        child = ARObject._find_child_element(element, "ECU-EXTRACT-VERSION")
        if child is not None:
            ecu_extract_version_value = child.text
            obj.ecu_extract_version = ecu_extract_version_value

        # Parse fibex_elements (list from container "FIBEX-ELEMENTS")
        obj.fibex_elements = []
        container = ARObject._find_child_element(element, "FIBEX-ELEMENTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.fibex_elements.append(child_value)

        # Parse interpolation_routines (list from container "INTERPOLATION-ROUTINES")
        obj.interpolation_routines = []
        container = ARObject._find_child_element(element, "INTERPOLATION-ROUTINES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.interpolation_routines.append(child_value)

        # Parse j1939_shared_addresses (list from container "J1939-SHARED-ADDRESSES")
        obj.j1939_shared_addresses = []
        container = ARObject._find_child_element(element, "J1939-SHARED-ADDRESSES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.j1939_shared_addresses.append(child_value)

        # Parse mapping_refs (list from container "MAPPINGS")
        obj.mapping_refs = []
        container = ARObject._find_child_element(element, "MAPPINGS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.mapping_refs.append(child_value)

        # Parse pnc_vector
        child = ARObject._find_child_element(element, "PNC-VECTOR")
        if child is not None:
            pnc_vector_value = child.text
            obj.pnc_vector = pnc_vector_value

        # Parse pnc_vector_offset
        child = ARObject._find_child_element(element, "PNC-VECTOR-OFFSET")
        if child is not None:
            pnc_vector_offset_value = child.text
            obj.pnc_vector_offset = pnc_vector_offset_value

        # Parse root_software
        child = ARObject._find_child_element(element, "ROOT-SOFTWARE")
        if child is not None:
            root_software_value = ARObject._deserialize_by_tag(child, "RootSwCompositionPrototype")
            obj.root_software = root_software_value

        # Parse sw_clusters (list from container "SW-CLUSTERS")
        obj.sw_clusters = []
        container = ARObject._find_child_element(element, "SW-CLUSTERS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.sw_clusters.append(child_value)

        # Parse systems (list from container "SYSTEMS")
        obj.systems = []
        container = ARObject._find_child_element(element, "SYSTEMS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.systems.append(child_value)

        # Parse system_version
        child = ARObject._find_child_element(element, "SYSTEM-VERSION")
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
