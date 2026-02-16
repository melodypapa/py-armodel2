"""NonqueuedReceiverComSpec AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

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
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "alive_timeout": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # aliveTimeout
        "enable_update": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # enableUpdate
        "filter": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DataFilter,
        ),  # filter
        "handle_data": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # handleData
        "handle_never": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # handleNever
        "handle_timeout_enum": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=HandleTimeoutEnum,
        ),  # handleTimeoutEnum
        "init_value": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ValueSpecification,
        ),  # initValue
        "timeout": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ValueSpecification,
        ),  # timeout
    }

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
