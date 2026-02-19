"""DataTransformation AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 149)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 763)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Transformer.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import (
    DataTransformationKindEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)


class DataTransformation(Identifiable):
    """AUTOSAR DataTransformation."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    data: Optional[DataTransformationKindEnum]
    execute_despite: Optional[Boolean]
    transformers: list[Any]
    def __init__(self) -> None:
        """Initialize DataTransformation."""
        super().__init__()
        self.data: Optional[DataTransformationKindEnum] = None
        self.execute_despite: Optional[Boolean] = None
        self.transformers: list[Any] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DataTransformation":
        """Deserialize XML element to DataTransformation object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DataTransformation object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse data
        child = ARObject._find_child_element(element, "DATA")
        if child is not None:
            data_value = child.text
            obj.data = data_value

        # Parse execute_despite
        child = ARObject._find_child_element(element, "EXECUTE-DESPITE")
        if child is not None:
            execute_despite_value = child.text
            obj.execute_despite = execute_despite_value

        # Parse transformers (list)
        obj.transformers = []
        for child in ARObject._find_all_child_elements(element, "TRANSFORMERS"):
            transformers_value = child.text
            obj.transformers.append(transformers_value)

        return obj



class DataTransformationBuilder:
    """Builder for DataTransformation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DataTransformation = DataTransformation()

    def build(self) -> DataTransformation:
        """Build and return DataTransformation object.

        Returns:
            DataTransformation instance
        """
        # TODO: Add validation
        return self._obj
