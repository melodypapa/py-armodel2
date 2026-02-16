"""SenderComSpec AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.p_port_com_spec import (
    PPortComSpec,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.autosar_data_prototype import (
    AutosarDataPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.composite_network_representation import (
    CompositeNetworkRepresentation,
)
from armodel.models.M2.MSR.DataDictionary.DataDefProperties.sw_data_def_props import (
    SwDataDefProps,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.transmission_com_spec_props import (
    TransmissionComSpecProps,
)


class SenderComSpec(PPortComSpec):
    """AUTOSAR SenderComSpec."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("composite_networks", None, False, True, CompositeNetworkRepresentation),  # compositeNetworks
        ("data_element", None, False, False, AutosarDataPrototype),  # dataElement
        ("handle_out_of_range", None, False, False, any (HandleOutOfRange)),  # handleOutOfRange
        ("network", None, False, False, SwDataDefProps),  # network
        ("transmission", None, False, False, any (Transmission)),  # transmission
        ("transmission_com_spec", None, False, False, TransmissionComSpecProps),  # transmissionComSpec
        ("uses_end_to_end", None, True, False, None),  # usesEndToEnd
    ]

    def __init__(self) -> None:
        """Initialize SenderComSpec."""
        super().__init__()
        self.composite_networks: list[CompositeNetworkRepresentation] = []
        self.data_element: Optional[AutosarDataPrototype] = None
        self.handle_out_of_range: Optional[Any] = None
        self.network: Optional[SwDataDefProps] = None
        self.transmission: Optional[Any] = None
        self.transmission_com_spec: Optional[TransmissionComSpecProps] = None
        self.uses_end_to_end: Optional[Boolean] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SenderComSpec to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SenderComSpec":
        """Create SenderComSpec from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SenderComSpec instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SenderComSpec since parent returns ARObject
        return cast("SenderComSpec", obj)


class SenderComSpecBuilder:
    """Builder for SenderComSpec."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SenderComSpec = SenderComSpec()

    def build(self) -> SenderComSpec:
        """Build and return SenderComSpec object.

        Returns:
            SenderComSpec instance
        """
        # TODO: Add validation
        return self._obj
