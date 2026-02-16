"""NonqueuedSenderComSpec AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.sender_com_spec import (
    SenderComSpec,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Filter.data_filter import (
    DataFilter,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.value_specification import (
    ValueSpecification,
)


class NonqueuedSenderComSpec(SenderComSpec):
    """AUTOSAR NonqueuedSenderComSpec."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("data_filter", None, False, False, DataFilter),  # dataFilter
        ("init_value", None, False, False, ValueSpecification),  # initValue
    ]

    def __init__(self) -> None:
        """Initialize NonqueuedSenderComSpec."""
        super().__init__()
        self.data_filter: Optional[DataFilter] = None
        self.init_value: Optional[ValueSpecification] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert NonqueuedSenderComSpec to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "NonqueuedSenderComSpec":
        """Create NonqueuedSenderComSpec from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            NonqueuedSenderComSpec instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to NonqueuedSenderComSpec since parent returns ARObject
        return cast("NonqueuedSenderComSpec", obj)


class NonqueuedSenderComSpecBuilder:
    """Builder for NonqueuedSenderComSpec."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: NonqueuedSenderComSpec = NonqueuedSenderComSpec()

    def build(self) -> NonqueuedSenderComSpec:
        """Build and return NonqueuedSenderComSpec object.

        Returns:
            NonqueuedSenderComSpec instance
        """
        # TODO: Add validation
        return self._obj
