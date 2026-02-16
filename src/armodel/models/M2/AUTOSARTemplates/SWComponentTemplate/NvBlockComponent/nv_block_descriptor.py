"""NvBlockDescriptor AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
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
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("client_server_ports", None, False, True, RoleBasedPortAssignment),  # clientServerPorts
        ("constant_values", None, False, True, ConstantSpecification),  # constantValues
        ("data_types", None, False, True, DataTypeMappingSet),  # dataTypes
        ("instantiation_data_defs", None, False, True, InstantiationDataDefProps),  # instantiationDataDefs
        ("mode_switch_events", None, False, True, any (ModeSwitchEvent)),  # modeSwitchEvents
        ("nv_block_datas", None, False, True, NvBlockDataMapping),  # nvBlockDatas
        ("nv_block_needs", None, False, False, NvBlockNeeds),  # nvBlockNeeds
        ("ram_block", None, False, False, VariableDataPrototype),  # ramBlock
        ("rom_block", None, False, False, ParameterDataPrototype),  # romBlock
        ("support_dirty", None, True, False, None),  # supportDirty
        ("timing_event", None, False, False, TimingEvent),  # timingEvent
        ("writing_strategies", None, False, True, any (RoleBasedData)),  # writingStrategies
    ]

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

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert NvBlockDescriptor to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "NvBlockDescriptor":
        """Create NvBlockDescriptor from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            NvBlockDescriptor instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to NvBlockDescriptor since parent returns ARObject
        return cast("NvBlockDescriptor", obj)


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
