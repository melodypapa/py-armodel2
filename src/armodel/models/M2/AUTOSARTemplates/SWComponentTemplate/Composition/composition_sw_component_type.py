"""CompositionSwComponentType AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 307)
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 291)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 75)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 895)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 219)
  - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (page 21)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 434)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Composition.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.sw_component_type import (
    SwComponentType,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.constant_specification import (
    ConstantSpecification,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes.data_type_mapping_set import (
    DataTypeMappingSet,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.instantiation_rte_event_props import (
    InstantiationRTEEventProps,
)
from armodel.models.M2.MSR.AsamHdo.Units.physical_dimension import (
    PhysicalDimension,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.sw_connector import (
    SwConnector,
)


class CompositionSwComponentType(SwComponentType):
    """AUTOSAR CompositionSwComponentType."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "components": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=any (SwComponent),
        ),  # components
        "connectors": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=SwConnector,
        ),  # connectors
        "constant_values": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=ConstantSpecification,
        ),  # constantValues
        "data_types": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=DataTypeMappingSet,
        ),  # dataTypes
        "instantiation_rte_events": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=InstantiationRTEEventProps,
        ),  # instantiationRTEEvents
        "physical": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=PhysicalDimension,
        ),  # physical
    }

    def __init__(self) -> None:
        """Initialize CompositionSwComponentType."""
        super().__init__()
        self.components: list[Any] = []
        self.connectors: list[SwConnector] = []
        self.constant_values: list[ConstantSpecification] = []
        self.data_types: list[DataTypeMappingSet] = []
        self.instantiation_rte_events: list[InstantiationRTEEventProps] = []
        self.physical: Optional[PhysicalDimension] = None


class CompositionSwComponentTypeBuilder:
    """Builder for CompositionSwComponentType."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CompositionSwComponentType = CompositionSwComponentType()

    def build(self) -> CompositionSwComponentType:
        """Build and return CompositionSwComponentType object.

        Returns:
            CompositionSwComponentType instance
        """
        # TODO: Add validation
        return self._obj
