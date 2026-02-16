"""NonqueuedReceiverComSpec AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.receiver_com_spec import (
    ReceiverComSpec,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Filter.data_filter import (
    DataFilter,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.value_specification import (
    ValueSpecification,
)


class NonqueuedReceiverComSpec(ReceiverComSpec):
    """AUTOSAR NonqueuedReceiverComSpec."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("alive_timeout", None, True, False, None),  # aliveTimeout
        ("enable_update", None, True, False, None),  # enableUpdate
        ("filter", None, False, False, DataFilter),  # filter
        ("handle_data", None, True, False, None),  # handleData
        ("handle_never", None, True, False, None),  # handleNever
        ("handle_timeout_enum", None, False, False, HandleTimeoutEnum),  # handleTimeoutEnum
        ("init_value", None, False, False, ValueSpecification),  # initValue
        ("timeout", None, False, False, ValueSpecification),  # timeout
    ]

    def __init__(self) -> None:
        """Initialize NonqueuedReceiverComSpec."""
        super().__init__()
        self.alive_timeout: Optional[TimeValue] = None
        self.enable_update: Optional[Boolean] = None
        self.filter: Optional[DataFilter] = None
        self.handle_data: Optional[Boolean] = None
        self.handle_never: Optional[Boolean] = None
        self.handle_timeout_enum: Optional[HandleTimeoutEnum] = None
        self.init_value: Optional[ValueSpecification] = None
        self.timeout: Optional[ValueSpecification] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert NonqueuedReceiverComSpec to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "NonqueuedReceiverComSpec":
        """Create NonqueuedReceiverComSpec from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            NonqueuedReceiverComSpec instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to NonqueuedReceiverComSpec since parent returns ARObject
        return cast("NonqueuedReceiverComSpec", obj)


class NonqueuedReceiverComSpecBuilder:
    """Builder for NonqueuedReceiverComSpec."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: NonqueuedReceiverComSpec = NonqueuedReceiverComSpec()

    def build(self) -> NonqueuedReceiverComSpec:
        """Build and return NonqueuedReceiverComSpec object.

        Returns:
            NonqueuedReceiverComSpec instance
        """
        # TODO: Add validation
        return self._obj
