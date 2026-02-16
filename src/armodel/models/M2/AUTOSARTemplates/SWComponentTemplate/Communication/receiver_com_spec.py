"""ReceiverComSpec AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.r_port_com_spec import (
    RPortComSpec,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.autosar_data_prototype import (
    AutosarDataPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.composite_network_representation import (
    CompositeNetworkRepresentation,
)


class ReceiverComSpec(RPortComSpec):
    """AUTOSAR ReceiverComSpec."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("composite_networks", None, False, True, CompositeNetworkRepresentation),  # compositeNetworks
        ("data_element", None, False, False, AutosarDataPrototype),  # dataElement
        ("handle_out_of_range", None, False, False, any (HandleOutOfRange)),  # handleOutOfRange
        ("max_delta", None, True, False, None),  # maxDelta
        ("sync_counter_init", None, True, False, None),  # syncCounterInit
        ("transformation_coms", None, False, True, any (TransformationCom)),  # transformationComs
        ("uses_end_to_end", None, True, False, None),  # usesEndToEnd
    ]

    def __init__(self) -> None:
        """Initialize ReceiverComSpec."""
        super().__init__()
        self.composite_networks: list[CompositeNetworkRepresentation] = []
        self.data_element: Optional[AutosarDataPrototype] = None
        self.handle_out_of_range: Optional[Any] = None
        self.max_delta: Optional[PositiveInteger] = None
        self.sync_counter_init: Optional[PositiveInteger] = None
        self.transformation_coms: list[Any] = []
        self.uses_end_to_end: Optional[Boolean] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ReceiverComSpec to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ReceiverComSpec":
        """Create ReceiverComSpec from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ReceiverComSpec instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ReceiverComSpec since parent returns ARObject
        return cast("ReceiverComSpec", obj)


class ReceiverComSpecBuilder:
    """Builder for ReceiverComSpec."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ReceiverComSpec = ReceiverComSpec()

    def build(self) -> ReceiverComSpec:
        """Build and return ReceiverComSpec object.

        Returns:
            ReceiverComSpec instance
        """
        # TODO: Add validation
        return self._obj
