"""NonqueuedSenderComSpec AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 179)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 198)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Communication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
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

    data_filter: Optional[DataFilter]
    init_value: Optional[ValueSpecification]
    def __init__(self) -> None:
        """Initialize NonqueuedSenderComSpec."""
        super().__init__()
        self.data_filter: Optional[DataFilter] = None
        self.init_value: Optional[ValueSpecification] = None


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
