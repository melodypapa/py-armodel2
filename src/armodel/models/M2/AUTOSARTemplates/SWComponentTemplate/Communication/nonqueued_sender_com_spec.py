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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Filter.data_filter import (
    DataFilter,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.value_specification import (
        ValueSpecification,
    )



class NonqueuedSenderComSpec(SenderComSpec):
    """AUTOSAR NonqueuedSenderComSpec."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    data_filter: Optional[DataFilter]
    init_value: Optional[ValueSpecification]
    def __init__(self) -> None:
        """Initialize NonqueuedSenderComSpec."""
        super().__init__()
        self.data_filter: Optional[DataFilter] = None
        self.init_value: Optional[ValueSpecification] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "NonqueuedSenderComSpec":
        """Deserialize XML element to NonqueuedSenderComSpec object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized NonqueuedSenderComSpec object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(NonqueuedSenderComSpec, cls).deserialize(element)

        # Parse data_filter
        child = ARObject._find_child_element(element, "DATA-FILTER")
        if child is not None:
            data_filter_value = ARObject._deserialize_by_tag(child, "DataFilter")
            obj.data_filter = data_filter_value

        # Parse init_value
        child = ARObject._find_child_element(element, "INIT-VALUE")
        if child is not None:
            init_value_value = ARObject._deserialize_by_tag(child, "ValueSpecification")
            obj.init_value = init_value_value

        return obj



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
