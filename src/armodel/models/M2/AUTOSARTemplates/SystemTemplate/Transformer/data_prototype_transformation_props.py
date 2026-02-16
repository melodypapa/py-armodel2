"""DataPrototypeTransformationProps AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.data_prototype import (
    DataPrototype,
)
from armodel.models.M2.MSR.DataDictionary.DataDefProperties.sw_data_def_props import (
    SwDataDefProps,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.transformation_props import (
    TransformationProps,
)


class DataPrototypeTransformationProps(ARObject):
    """AUTOSAR DataPrototypeTransformationProps."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("data_prototype_in", None, False, False, DataPrototype),  # dataPrototypeIn
        ("network", None, False, False, SwDataDefProps),  # network
        ("transformation_props", None, False, False, TransformationProps),  # transformationProps
    ]

    def __init__(self) -> None:
        """Initialize DataPrototypeTransformationProps."""
        super().__init__()
        self.data_prototype_in: Optional[DataPrototype] = None
        self.network: Optional[SwDataDefProps] = None
        self.transformation_props: Optional[TransformationProps] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DataPrototypeTransformationProps to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DataPrototypeTransformationProps":
        """Create DataPrototypeTransformationProps from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DataPrototypeTransformationProps instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DataPrototypeTransformationProps since parent returns ARObject
        return cast("DataPrototypeTransformationProps", obj)


class DataPrototypeTransformationPropsBuilder:
    """Builder for DataPrototypeTransformationProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DataPrototypeTransformationProps = DataPrototypeTransformationProps()

    def build(self) -> DataPrototypeTransformationProps:
        """Build and return DataPrototypeTransformationProps object.

        Returns:
            DataPrototypeTransformationProps instance
        """
        # TODO: Add validation
        return self._obj
