"""DataTypeMap AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 232)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2015)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Datatype_Datatypes.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ImplementationDataTypes.abstract_implementation_data_type import (
    AbstractImplementationDataType,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes.application_data_type import (
    ApplicationDataType,
)


class DataTypeMap(ARObject):
    """AUTOSAR DataTypeMap."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "application_data_type": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ApplicationDataType,
        ),  # applicationDataType
        "implementation": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=AbstractImplementationDataType,
        ),  # implementation
    }

    def __init__(self) -> None:
        """Initialize DataTypeMap."""
        super().__init__()
        self.application_data_type: Optional[ApplicationDataType] = None
        self.implementation: Optional[AbstractImplementationDataType] = None


class DataTypeMapBuilder:
    """Builder for DataTypeMap."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DataTypeMap = DataTypeMap()

    def build(self) -> DataTypeMap:
        """Build and return DataTypeMap object.

        Returns:
            DataTypeMap instance
        """
        # TODO: Add validation
        return self._obj
