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
    @classmethod
    def deserialize(cls, element: ET.Element) -> "System":
        """Deserialize XML element to System object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized System object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse client_id_refs (list)
        obj.client_id_refs = []
        for child in ARObject._find_all_child_elements(element, "CLIENT-IDS"):
            client_id_refs_value = ARObject._deserialize_by_tag(child, "ClientIdDefinitionSet")
            obj.client_id_refs.append(client_id_refs_value)

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

        # Parse fibex_elements (list)
        obj.fibex_elements = []
        for child in ARObject._find_all_child_elements(element, "FIBEX-ELEMENTS"):
            fibex_elements_value = ARObject._deserialize_by_tag(child, "FibexElement")
            obj.fibex_elements.append(fibex_elements_value)

        # Parse interpolation_routines (list)
        obj.interpolation_routines = []
        for child in ARObject._find_all_child_elements(element, "INTERPOLATION-ROUTINES"):
            interpolation_routines_value = ARObject._deserialize_by_tag(child, "InterpolationRoutine")
            obj.interpolation_routines.append(interpolation_routines_value)

        # Parse j1939_shared_addresses (list)
        obj.j1939_shared_addresses = []
        for child in ARObject._find_all_child_elements(element, "J1939-SHARED-ADDRESSES"):
            j1939_shared_addresses_value = ARObject._deserialize_by_tag(child, "J1939SharedAddressCluster")
            obj.j1939_shared_addresses.append(j1939_shared_addresses_value)

        # Parse mapping_refs (list)
        obj.mapping_refs = []
        for child in ARObject._find_all_child_elements(element, "MAPPINGS"):
            mapping_refs_value = ARObject._deserialize_by_tag(child, "SystemMapping")
            obj.mapping_refs.append(mapping_refs_value)

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

        # Parse sw_clusters (list)
        obj.sw_clusters = []
        for child in ARObject._find_all_child_elements(element, "SW-CLUSTERS"):
            sw_clusters_value = ARObject._deserialize_by_tag(child, "CpSoftwareCluster")
            obj.sw_clusters.append(sw_clusters_value)

        # Parse systems (list)
        obj.systems = []
        for child in ARObject._find_all_child_elements(element, "SYSTEMS"):
            systems_value = ARObject._deserialize_by_tag(child, "Chapter")
            obj.systems.append(systems_value)

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
