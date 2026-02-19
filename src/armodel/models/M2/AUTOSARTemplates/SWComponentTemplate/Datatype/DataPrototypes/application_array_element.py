"""ApplicationArrayElement AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 252)
  - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (page 43)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Datatype_DataPrototypes.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.application_composite_element_data_prototype import (
    ApplicationCompositeElementDataPrototype,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ImplementationDataTypes import (
    ArraySizeSemanticsEnum,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes import (
    ArraySizeHandlingEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes.application_primitive_data_type import (
        ApplicationPrimitiveDataType,
    )



class ApplicationArrayElement(ApplicationCompositeElementDataPrototype):
    """AUTOSAR ApplicationArrayElement."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    array_size_handling: Optional[ArraySizeHandlingEnum]
    array_size: Optional[ArraySizeSemanticsEnum]
    index_data_type: Optional[ApplicationPrimitiveDataType]
    max_number_of: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize ApplicationArrayElement."""
        super().__init__()
        self.array_size_handling: Optional[ArraySizeHandlingEnum] = None
        self.array_size: Optional[ArraySizeSemanticsEnum] = None
        self.index_data_type: Optional[ApplicationPrimitiveDataType] = None
        self.max_number_of: Optional[PositiveInteger] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "ApplicationArrayElement":
        """Deserialize XML element to ApplicationArrayElement object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ApplicationArrayElement object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse array_size_handling
        child = ARObject._find_child_element(element, "ARRAY-SIZE-HANDLING")
        if child is not None:
            array_size_handling_value = child.text
            obj.array_size_handling = array_size_handling_value

        # Parse array_size
        child = ARObject._find_child_element(element, "ARRAY-SIZE")
        if child is not None:
            array_size_value = child.text
            obj.array_size = array_size_value

        # Parse index_data_type
        child = ARObject._find_child_element(element, "INDEX-DATA-TYPE")
        if child is not None:
            index_data_type_value = ARObject._deserialize_by_tag(child, "ApplicationPrimitiveDataType")
            obj.index_data_type = index_data_type_value

        # Parse max_number_of
        child = ARObject._find_child_element(element, "MAX-NUMBER-OF")
        if child is not None:
            max_number_of_value = child.text
            obj.max_number_of = max_number_of_value

        return obj



class ApplicationArrayElementBuilder:
    """Builder for ApplicationArrayElement."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ApplicationArrayElement = ApplicationArrayElement()

    def build(self) -> ApplicationArrayElement:
        """Build and return ApplicationArrayElement object.

        Returns:
            ApplicationArrayElement instance
        """
        # TODO: Add validation
        return self._obj
