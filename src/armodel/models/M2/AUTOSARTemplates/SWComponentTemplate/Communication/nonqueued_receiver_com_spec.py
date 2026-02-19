"""NonqueuedReceiverComSpec AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 172)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2039)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 198)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Communication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.receiver_com_spec import (
    ReceiverComSpec,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import (
    HandleTimeoutEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Filter.data_filter import (
    DataFilter,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.value_specification import (
        ValueSpecification,
    )



class NonqueuedReceiverComSpec(ReceiverComSpec):
    """AUTOSAR NonqueuedReceiverComSpec."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    alive_timeout: Optional[TimeValue]
    enable_update: Optional[Boolean]
    filter: Optional[DataFilter]
    handle_data: Optional[Boolean]
    handle_never: Optional[Boolean]
    handle_timeout_enum: Optional[HandleTimeoutEnum]
    init_value: Optional[ValueSpecification]
    timeout: Optional[ValueSpecification]
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
    @classmethod
    def deserialize(cls, element: ET.Element) -> "NonqueuedReceiverComSpec":
        """Deserialize XML element to NonqueuedReceiverComSpec object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized NonqueuedReceiverComSpec object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(NonqueuedReceiverComSpec, cls).deserialize(element)

        # Parse alive_timeout
        child = ARObject._find_child_element(element, "ALIVE-TIMEOUT")
        if child is not None:
            alive_timeout_value = child.text
            obj.alive_timeout = alive_timeout_value

        # Parse enable_update
        child = ARObject._find_child_element(element, "ENABLE-UPDATE")
        if child is not None:
            enable_update_value = child.text
            obj.enable_update = enable_update_value

        # Parse filter
        child = ARObject._find_child_element(element, "FILTER")
        if child is not None:
            filter_value = ARObject._deserialize_by_tag(child, "DataFilter")
            obj.filter = filter_value

        # Parse handle_data
        child = ARObject._find_child_element(element, "HANDLE-DATA")
        if child is not None:
            handle_data_value = child.text
            obj.handle_data = handle_data_value

        # Parse handle_never
        child = ARObject._find_child_element(element, "HANDLE-NEVER")
        if child is not None:
            handle_never_value = child.text
            obj.handle_never = handle_never_value

        # Parse handle_timeout_enum
        child = ARObject._find_child_element(element, "HANDLE-TIMEOUT-ENUM")
        if child is not None:
            handle_timeout_enum_value = HandleTimeoutEnum.deserialize(child)
            obj.handle_timeout_enum = handle_timeout_enum_value

        # Parse init_value
        child = ARObject._find_child_element(element, "INIT-VALUE")
        if child is not None:
            init_value_value = ARObject._deserialize_by_tag(child, "ValueSpecification")
            obj.init_value = init_value_value

        # Parse timeout
        child = ARObject._find_child_element(element, "TIMEOUT")
        if child is not None:
            timeout_value = ARObject._deserialize_by_tag(child, "ValueSpecification")
            obj.timeout = timeout_value

        return obj



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
