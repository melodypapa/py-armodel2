"""DataPrototypeMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 125)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2014)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_PortInterface.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.autosar_data_prototype import (
    AutosarDataPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.data_transformation import (
    DataTransformation,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.sub_element_mapping import (
    SubElementMapping,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.text_table_mapping import (
    TextTableMapping,
)


class DataPrototypeMapping(ARObject):
    """AUTOSAR DataPrototypeMapping."""

    first_data: Optional[AutosarDataPrototype]
    first_to_second: Optional[DataTransformation]
    second_data: Optional[AutosarDataPrototype]
    second_to_first: Optional[DataTransformation]
    sub_elements: list[SubElementMapping]
    text_table: TextTableMapping
    def __init__(self) -> None:
        """Initialize DataPrototypeMapping."""
        super().__init__()
        self.first_data: Optional[AutosarDataPrototype] = None
        self.first_to_second: Optional[DataTransformation] = None
        self.second_data: Optional[AutosarDataPrototype] = None
        self.second_to_first: Optional[DataTransformation] = None
        self.sub_elements: list[SubElementMapping] = []
        self.text_table: TextTableMapping = None


class DataPrototypeMappingBuilder:
    """Builder for DataPrototypeMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DataPrototypeMapping = DataPrototypeMapping()

    def build(self) -> DataPrototypeMapping:
        """Build and return DataPrototypeMapping object.

        Returns:
            DataPrototypeMapping instance
        """
        # TODO: Add validation
        return self._obj
