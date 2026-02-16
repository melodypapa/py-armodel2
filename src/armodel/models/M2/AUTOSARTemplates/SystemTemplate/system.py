"""System AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
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
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("client_ids", None, False, True, ClientIdDefinitionSet),  # clientIds
        ("container_i_pdu_header_byte", None, False, False, any (ByteOrderEnumOrder)),  # containerIPduHeaderByte
        ("ecu_extract_version", None, True, False, None),  # ecuExtractVersion
        ("fibex_elements", None, False, True, FibexElement),  # fibexElements
        ("interpolation_routines", None, False, True, InterpolationRoutine),  # interpolationRoutines
        ("j1939_shared_addresses", None, False, True, J1939SharedAddressCluster),  # j1939SharedAddresses
        ("mappings", None, False, True, SystemMapping),  # mappings
        ("pnc_vector", None, True, False, None),  # pncVector
        ("pnc_vector_offset", None, True, False, None),  # pncVectorOffset
        ("root_software", None, False, False, RootSwCompositionPrototype),  # rootSoftware
        ("sw_clusters", None, False, True, CpSoftwareCluster),  # swClusters
        ("systems", None, False, True, Chapter),  # systems
        ("system_version", None, True, False, None),  # systemVersion
    ]

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

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert System to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "System":
        """Create System from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            System instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to System since parent returns ARObject
        return cast("System", obj)


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
