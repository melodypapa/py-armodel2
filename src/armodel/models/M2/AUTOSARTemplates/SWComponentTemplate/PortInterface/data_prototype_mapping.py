"""DataPrototypeMapping AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
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

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "first_data": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=AutosarDataPrototype,
        ),  # firstData
        "first_to_second": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DataTransformation,
        ),  # firstToSecond
        "second_data": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=AutosarDataPrototype,
        ),  # secondData
        "second_to_first": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DataTransformation,
        ),  # secondToFirst
        "sub_elements": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=SubElementMapping,
        ),  # subElements
        "text_table": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="1",
            element_class=TextTableMapping,
        ),  # textTable
    }

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
