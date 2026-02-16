"""EcuResourceEstimation AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.MSR.Documentation.BlockElements.documentation_block import (
    DocumentationBlock,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.ecu_instance import (
    EcuInstance,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.resource_consumption import (
    ResourceConsumption,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping.swc_to_ecu_mapping import (
    SwcToEcuMapping,
)


class EcuResourceEstimation(ARObject):
    """AUTOSAR EcuResourceEstimation."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("bsw_resource", None, False, False, ResourceConsumption),  # bswResource
        ("ecu_instance", None, False, False, EcuInstance),  # ecuInstance
        ("introduction", None, False, False, DocumentationBlock),  # introduction
        ("rte_resource", None, False, False, ResourceConsumption),  # rteResource
        ("sw_comp_to_ecus", None, False, True, SwcToEcuMapping),  # swCompToEcus
    ]

    def __init__(self) -> None:
        """Initialize EcuResourceEstimation."""
        super().__init__()
        self.bsw_resource: Optional[ResourceConsumption] = None
        self.ecu_instance: Optional[EcuInstance] = None
        self.introduction: Optional[DocumentationBlock] = None
        self.rte_resource: Optional[ResourceConsumption] = None
        self.sw_comp_to_ecus: list[SwcToEcuMapping] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert EcuResourceEstimation to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcuResourceEstimation":
        """Create EcuResourceEstimation from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            EcuResourceEstimation instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to EcuResourceEstimation since parent returns ARObject
        return cast("EcuResourceEstimation", obj)


class EcuResourceEstimationBuilder:
    """Builder for EcuResourceEstimation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcuResourceEstimation = EcuResourceEstimation()

    def build(self) -> EcuResourceEstimation:
        """Build and return EcuResourceEstimation object.

        Returns:
            EcuResourceEstimation instance
        """
        # TODO: Add validation
        return self._obj
