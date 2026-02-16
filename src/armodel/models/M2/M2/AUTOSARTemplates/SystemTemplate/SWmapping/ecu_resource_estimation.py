"""EcuResourceEstimation AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

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
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "bsw_resource": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ResourceConsumption,
        ),  # bswResource
        "ecu_instance": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=EcuInstance,
        ),  # ecuInstance
        "introduction": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DocumentationBlock,
        ),  # introduction
        "rte_resource": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ResourceConsumption,
        ),  # rteResource
        "sw_comp_to_ecus": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=SwcToEcuMapping,
        ),  # swCompToEcus
    }

    def __init__(self) -> None:
        """Initialize EcuResourceEstimation."""
        super().__init__()
        self.bsw_resource: Optional[ResourceConsumption] = None
        self.ecu_instance: Optional[EcuInstance] = None
        self.introduction: Optional[DocumentationBlock] = None
        self.rte_resource: Optional[ResourceConsumption] = None
        self.sw_comp_to_ecus: list[SwcToEcuMapping] = []


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
