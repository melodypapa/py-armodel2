"""NvBlockDescriptor AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.constant_specification import (
    ConstantSpecification,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes.data_type_mapping_set import (
    DataTypeMappingSet,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.InstantiationDataDefProps.instantiation_data_def_props import (
    InstantiationDataDefProps,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent.nv_block_data_mapping import (
    NvBlockDataMapping,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.nv_block_needs import (
    NvBlockNeeds,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.parameter_data_prototype import (
    ParameterDataPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ServiceMapping.role_based_port_assignment import (
    RoleBasedPortAssignment,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents.timing_event import (
    TimingEvent,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)


class NvBlockDescriptor(Identifiable):
    """AUTOSAR NvBlockDescriptor."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "client_server_ports": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=RoleBasedPortAssignment,
        ),  # clientServerPorts
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
        "instantiation_data_defs": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=InstantiationDataDefProps,
        ),  # instantiationDataDefs
        "mode_switch_events": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=any (ModeSwitchEvent),
        ),  # modeSwitchEvents
        "nv_block_datas": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=NvBlockDataMapping,
        ),  # nvBlockDatas
        "nv_block_needs": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=NvBlockNeeds,
        ),  # nvBlockNeeds
        "ram_block": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=VariableDataPrototype,
        ),  # ramBlock
        "rom_block": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ParameterDataPrototype,
        ),  # romBlock
        "support_dirty": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # supportDirty
        "timing_event": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=TimingEvent,
        ),  # timingEvent
        "writing_strategies": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=any (RoleBasedData),
        ),  # writingStrategies
    }

    def __init__(self) -> None:
        """Initialize NvBlockDescriptor."""
        super().__init__()
        self.client_server_ports: list[RoleBasedPortAssignment] = []
        self.constant_values: list[ConstantSpecification] = []
        self.data_types: list[DataTypeMappingSet] = []
        self.instantiation_data_defs: list[InstantiationDataDefProps] = []
        self.mode_switch_events: list[Any] = []
        self.nv_block_datas: list[NvBlockDataMapping] = []
        self.nv_block_needs: Optional[NvBlockNeeds] = None
        self.ram_block: Optional[VariableDataPrototype] = None
        self.rom_block: Optional[ParameterDataPrototype] = None
        self.support_dirty: Optional[Boolean] = None
        self.timing_event: Optional[TimingEvent] = None
        self.writing_strategies: list[Any] = []


class NvBlockDescriptorBuilder:
    """Builder for NvBlockDescriptor."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: NvBlockDescriptor = NvBlockDescriptor()

    def build(self) -> NvBlockDescriptor:
        """Build and return NvBlockDescriptor object.

        Returns:
            NvBlockDescriptor instance
        """
        # TODO: Add validation
        return self._obj
