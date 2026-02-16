"""IncludedDataTypeSet AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes.autosar_data_type import (
    AutosarDataType,
)


class IncludedDataTypeSet(ARObject):
    """AUTOSAR IncludedDataTypeSet."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "data_types": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=AutosarDataType,
        ),  # dataTypes
        "literal_prefix": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # literalPrefix
    }

    def __init__(self) -> None:
        """Initialize IncludedDataTypeSet."""
        super().__init__()
        self.data_types: list[AutosarDataType] = []
        self.literal_prefix: Optional[Identifier] = None


class IncludedDataTypeSetBuilder:
    """Builder for IncludedDataTypeSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IncludedDataTypeSet = IncludedDataTypeSet()

    def build(self) -> IncludedDataTypeSet:
        """Build and return IncludedDataTypeSet object.

        Returns:
            IncludedDataTypeSet instance
        """
        # TODO: Add validation
        return self._obj
