"""BswCalledEntity AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 74)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 972)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_module_entity import (
    BswModuleEntity,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class BswCalledEntity(BswModuleEntity):
    """AUTOSAR BswCalledEntity."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize BswCalledEntity."""
        super().__init__()
    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswCalledEntity":
        """Deserialize XML element to BswCalledEntity object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BswCalledEntity object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        return obj



class BswCalledEntityBuilder:
    """Builder for BswCalledEntity."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswCalledEntity = BswCalledEntity()

    def build(self) -> BswCalledEntity:
        """Build and return BswCalledEntity object.

        Returns:
            BswCalledEntity instance
        """
        # TODO: Add validation
        return self._obj
