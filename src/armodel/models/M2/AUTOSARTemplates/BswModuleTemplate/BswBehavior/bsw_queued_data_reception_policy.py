"""BswQueuedDataReceptionPolicy AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 105)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_data_reception_policy import (
    BswDataReceptionPolicy,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class BswQueuedDataReceptionPolicy(BswDataReceptionPolicy):
    """AUTOSAR BswQueuedDataReceptionPolicy."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    queue_length: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize BswQueuedDataReceptionPolicy."""
        super().__init__()
        self.queue_length: Optional[PositiveInteger] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswQueuedDataReceptionPolicy":
        """Deserialize XML element to BswQueuedDataReceptionPolicy object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BswQueuedDataReceptionPolicy object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse queue_length
        child = ARObject._find_child_element(element, "QUEUE-LENGTH")
        if child is not None:
            queue_length_value = child.text
            obj.queue_length = queue_length_value

        return obj



class BswQueuedDataReceptionPolicyBuilder:
    """Builder for BswQueuedDataReceptionPolicy."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswQueuedDataReceptionPolicy = BswQueuedDataReceptionPolicy()

    def build(self) -> BswQueuedDataReceptionPolicy:
        """Build and return BswQueuedDataReceptionPolicy object.

        Returns:
            BswQueuedDataReceptionPolicy instance
        """
        # TODO: Add validation
        return self._obj
