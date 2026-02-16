"""MetaDataItemSet AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.meta_data_item import (
    MetaDataItem,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)


class MetaDataItemSet(ARObject):
    """AUTOSAR MetaDataItemSet."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "data_elements": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=VariableDataPrototype,
        ),  # dataElements
        "meta_data_items": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=MetaDataItem,
        ),  # metaDataItems
    }

    def __init__(self) -> None:
        """Initialize MetaDataItemSet."""
        super().__init__()
        self.data_elements: list[VariableDataPrototype] = []
        self.meta_data_items: list[MetaDataItem] = []


class MetaDataItemSetBuilder:
    """Builder for MetaDataItemSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MetaDataItemSet = MetaDataItemSet()

    def build(self) -> MetaDataItemSet:
        """Build and return MetaDataItemSet object.

        Returns:
            MetaDataItemSet instance
        """
        # TODO: Add validation
        return self._obj
