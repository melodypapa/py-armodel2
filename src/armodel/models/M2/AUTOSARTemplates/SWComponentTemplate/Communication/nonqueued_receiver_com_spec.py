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
