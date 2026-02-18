"""MetaDataItem AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 98)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2037)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_PortInterface.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.text_value_specification import (
    TextValueSpecification,
)


class MetaDataItem(ARObject):
    """AUTOSAR MetaDataItem."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    length: Optional[PositiveInteger]
    meta_data_item: Optional[TextValueSpecification]
    def __init__(self) -> None:
        """Initialize MetaDataItem."""
        super().__init__()
        self.length: Optional[PositiveInteger] = None
        self.meta_data_item: Optional[TextValueSpecification] = None


class MetaDataItemBuilder:
    """Builder for MetaDataItem."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MetaDataItem = MetaDataItem()

    def build(self) -> MetaDataItem:
        """Build and return MetaDataItem object.

        Returns:
            MetaDataItem instance
        """
        # TODO: Add validation
        return self._obj
