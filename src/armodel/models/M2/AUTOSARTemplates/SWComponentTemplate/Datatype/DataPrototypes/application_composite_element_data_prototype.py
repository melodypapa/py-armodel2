"""ApplicationCompositeElementDataPrototype AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 306)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 1996)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Datatype_DataPrototypes.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.data_prototype import (
    DataPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes.application_data_type import (
    ApplicationDataType,
)
from abc import ABC, abstractmethod


class ApplicationCompositeElementDataPrototype(DataPrototype, ABC):
    """AUTOSAR ApplicationCompositeElementDataPrototype."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    type: Optional[ApplicationDataType]
    def __init__(self) -> None:
        """Initialize ApplicationCompositeElementDataPrototype."""
        super().__init__()
        self.type: Optional[ApplicationDataType] = None


class ApplicationCompositeElementDataPrototypeBuilder:
    """Builder for ApplicationCompositeElementDataPrototype."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ApplicationCompositeElementDataPrototype = ApplicationCompositeElementDataPrototype()

    def build(self) -> ApplicationCompositeElementDataPrototype:
        """Build and return ApplicationCompositeElementDataPrototype object.

        Returns:
            ApplicationCompositeElementDataPrototype instance
        """
        # TODO: Add validation
        return self._obj
