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
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
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

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "client_ids": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=ClientIdDefinitionSet,
        ),  # clientIds
        "container_i_pdu_header_byte": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (ByteOrderEnumOrder),
        ),  # containerIPduHeaderByte
        "ecu_extract_version": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # ecuExtractVersion
        "fibex_elements": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=FibexElement,
        ),  # fibexElements
        "interpolation_routines": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=InterpolationRoutine,
        ),  # interpolationRoutines
        "j1939_shared_addresses": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=J1939SharedAddressCluster,
        ),  # j1939SharedAddresses
        "mappings": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=SystemMapping,
        ),  # mappings
        "pnc_vector": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # pncVector
        "pnc_vector_offset": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # pncVectorOffset
        "root_software": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=RootSwCompositionPrototype,
        ),  # rootSoftware
        "sw_clusters": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=CpSoftwareCluster,
        ),  # swClusters
        "systems": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=Chapter,
        ),  # systems
        "system_version": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # systemVersion
    }

    def __init__(self) -> None:
        """Initialize System."""
        super().__init__()
        self.client_ids: list[ClientIdDefinitionSet] = []
        self.container_i_pdu_header_byte: Optional[Any] = None
        self.ecu_extract_version: Optional[RevisionLabelString] = None
        self.fibex_elements: list[FibexElement] = []
        self.interpolation_routines: list[InterpolationRoutine] = []
        self.j1939_shared_addresses: list[J1939SharedAddressCluster] = []
        self.mappings: list[SystemMapping] = []
        self.pnc_vector: Optional[PositiveInteger] = None
        self.pnc_vector_offset: Optional[PositiveInteger] = None
        self.root_software: Optional[RootSwCompositionPrototype] = None
        self.sw_clusters: list[CpSoftwareCluster] = []
        self.systems: list[Chapter] = []
        self.system_version: Optional[RevisionLabelString] = None


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
